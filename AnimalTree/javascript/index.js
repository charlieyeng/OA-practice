const express = require('express');
const bodyParser = require('body-parser');
const treeNode = require('./classes/treeNode');
const treeService = require('./services/treeService');

const { TreeNode } = treeNode;

const app = express();
const port = 3001;

let root = null;
function initializeTree() {
  const rootNode = new TreeNode(1, 'root', [new TreeNode(2, 'ant', []), new TreeNode(3, 'bear', [new TreeNode(4, 'cat', []), new TreeNode(5, 'dog', [new TreeNode(6, 'elephant', [])])]), new TreeNode(7, 'frog', [])]);
  return rootNode;
}
root = initializeTree();

app.use(bodyParser.json());
app.get('/', (req, res) => res.send('Hello World!'));

app.get('/api/tree', (req, res) => {
  const apiTree = treeService.getApiTree(root);
  res.status(200).json(apiTree);
});

app.post('/api/tree', (req, res) => {
  const { body } = req;
  if (
    !body.parent
          || !body.label
  ) {
    res.status(400).send({
      status: 'FAILED',
      data: {
        error: 'Missing required field',
      },
    });
  }

  const success = treeService.postApiTree(root, body.parent, body.label);

  if (!success) {
    res.status(404).send({
      STATUS: 'FAILED',
      data: {
        error: 'Could not find the parent',
      },
    });
  }
  res.status(201).json({
    message: 'Succcesfully added new animal',
  });
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));

module.exports = app;
