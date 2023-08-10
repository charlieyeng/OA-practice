const { v4: uuidv4 } = require('uuid');
const treeNode = require('../classes/treeNode');

const { TreeNode } = treeNode;
// Recursively map the children nodes to be the correct format
function formatChildren(root) {
  const newNode = {};
  newNode[root.id] = {
    label: root.label,
    children: root.children.length ? root.children.map((child) => formatChildren(child))
      : [],
  };
  return newNode;
}
// Serializes a tree given the root
function serialize(root, output) {
  if (!root) {
    return;
  }
  const newNode = {};
  newNode[root.id] = {
    label: root.label,
    children: root.children.length ? root.children.map((child) => formatChildren(child))
      : [],
  };

  if (newNode.children) {
    newNode.children.forEach((child) => {
      serialize(child, output);
    });
  }

  output.push(newNode);
}

// Traverse the created tree using preorder traversal
function findParentAndInsert(root, parent, label) {
  // parent is found, we push node onto the tree
  if (String(root.id) === String(parent)) {
    root.children.push(new TreeNode(uuidv4(), label, []));
    return true;
  }

  if (root.children) {
    let res = false;
    root.children.forEach((child) => {
      res = res || findParentAndInsert(child, parent, label);
    });
    return res;
  }

  // parent is never found, so we did not insert the node into the tree
  return false;
}
// Function that gets current tree given root
const getApiTree = (root) => {
  const output = [];
  serialize(root, output);
  return output;
};

// Function that finds a parent and appends a new element to the tree
const postApiTree = (root, parent, label) => findParentAndInsert(root, parent, label);

module.exports = {
  getApiTree,
  postApiTree,
};
