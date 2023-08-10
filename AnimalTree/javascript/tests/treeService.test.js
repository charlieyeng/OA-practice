const treeNode = require('../classes/treeNode');

const { TreeNode } = treeNode;
const treeService = require('../services/treeService');

jest.mock('uuid', () => ({ v4: () => '0' }));

describe('GET /api/tree', () => {
  test('Successfully get sample tree in correct format', () => {
    const testRoot = new TreeNode(1, 'root', [new TreeNode(2, 'ant', []), new TreeNode(3, 'bear', [new TreeNode(4, 'cat', []), new TreeNode(5, 'dog', [new TreeNode(6, 'elephant', [])])]), new TreeNode(7, 'frog', [])]);
    const exampleResult = [
      {
        1: {
          label: 'root',
          children: [
            {
              2: {
                label: 'ant',
                children: [],
              },
            },
            {
              3: {
                label: 'bear',
                children: [
                  {
                    4: {
                      label: 'cat',
                      children: [],
                    },
                  },
                  {
                    5: {
                      label: 'dog',
                      children: [
                        {
                          6: {
                            label: 'elephant',
                            children: [],
                          },
                        },
                      ],
                    },
                  },
                ],
              },
            },
            {
              7: {
                label: 'frog',
                children: [],
              },
            },
          ],
        },
      },
    ];
    expect(treeService.getApiTree(testRoot)).toStrictEqual(exampleResult);
  });

  test('Null root node shoud return an empty array', () => {
    const testRoot = null;
    expect(treeService.getApiTree(testRoot)).toStrictEqual([]);
  });
});

describe('POST /api/tree', () => {
  test('Successfully find parent and insert a new node into the root tree', () => {
    const testRoot = new TreeNode(1, 'root', [new TreeNode(2, 'ant', []), new TreeNode(3, 'bear', [new TreeNode(4, 'cat', []), new TreeNode(5, 'dog', [new TreeNode(6, 'elephant', [])])]), new TreeNode(7, 'frog', [])]);
    const exampleResult = [
      {
        1: {
          label: 'root',
          children: [
            {
              2: {
                label: 'ant',
                children: [],
              },
            },
            {
              3: {
                label: 'bear',
                children: [
                  {
                    4: {
                      label: 'cat',
                      children: [],
                    },
                  },
                  {
                    5: {
                      label: 'dog',
                      children: [
                        {
                          6: {
                            label: 'elephant',
                            children: [],
                          },
                        },
                      ],
                    },
                  },
                ],
              },
            },
            {
              7: {
                label: 'frog',
                children: [],
              },
            },
            {
              0: {
                label: 'monkey',
                children: [],
              },
            },
          ],
        },
      },
    ];
    expect(treeService.postApiTree(testRoot, '1', 'monkey')).toStrictEqual(true);
    expect(treeService.getApiTree(testRoot)).toStrictEqual(exampleResult);
  });

  test('Successfully find parent and insert a new node into a child in the tree', () => {
    const testRoot = new TreeNode(1, 'root', [new TreeNode(2, 'ant', []), new TreeNode(3, 'bear', [new TreeNode(4, 'cat', []), new TreeNode(5, 'dog', [new TreeNode(6, 'elephant', [])])]), new TreeNode(7, 'frog', [])]);
    const exampleResult = [
      {
        1: {
          label: 'root',
          children: [
            {
              2: {
                label: 'ant',
                children: [],
              },
            },
            {
              3: {
                label: 'bear',
                children: [
                  {
                    4: {
                      label: 'cat',
                      children: [],
                    },
                  },
                  {
                    5: {
                      label: 'dog',
                      children: [
                        {
                          6: {
                            label: 'elephant',
                            children: [
                              {
                                0: {
                                  label: 'monkey',
                                  children: [],
                                },
                              },
                            ],
                          },
                        },
                      ],
                    },
                  },
                ],
              },
            },
            {
              7: {
                label: 'frog',
                children: [],
              },
            },
          ],
        },
      },
    ];
    expect(treeService.postApiTree(testRoot, '6', 'monkey')).toStrictEqual(true);
    expect(treeService.getApiTree(testRoot)).toStrictEqual(exampleResult);
  });

  test('Parent is not found and the tree is unchanged', () => {
    const testRoot = new TreeNode(1, 'root', [new TreeNode(2, 'ant', []), new TreeNode(3, 'bear', [new TreeNode(4, 'cat', []), new TreeNode(5, 'dog', [new TreeNode(6, 'elephant', [])])]), new TreeNode(7, 'frog', [])]);
    const exampleResult = [
      {
        1: {
          label: 'root',
          children: [
            {
              2: {
                label: 'ant',
                children: [],
              },
            },
            {
              3: {
                label: 'bear',
                children: [
                  {
                    4: {
                      label: 'cat',
                      children: [],
                    },
                  },
                  {
                    5: {
                      label: 'dog',
                      children: [
                        {
                          6: {
                            label: 'elephant',
                            children: [],
                          },
                        },
                      ],
                    },
                  },
                ],
              },
            },
            {
              7: {
                label: 'frog',
                children: [],
              },
            },
          ],
        },
      },
    ];
    expect(treeService.postApiTree(testRoot, '8', 'monkey')).toStrictEqual(false);
    expect(treeService.getApiTree(testRoot)).toStrictEqual(exampleResult);
  });
});
