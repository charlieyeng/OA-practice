# Javascript

Before you get started, make sure you have node installed and configured correctly. 

To build, open your terminal and navigate to the `javascript` directory in this project and run `npm install`.

To start your server, run `node index.js`.  Open up your favorite browser and navigate to http://localhost:3001/ and you should see "Hello World!".

To run tests for the project, run `npm test`.

To lint the project, run `npm run lint`.

Now follow the steps outlined in [The Problem](https://github.com/hinge-health/interviews-services#the-problem)


## Introduction
This code repo houses the candidate solution to the Hinge Health technical exercise. The tree is created in memory using a TreeNode class. The TreeNode has values of `id`, `label`, and `children` and has been initialized to the sample tree given in the GitHub repo. This mimics previous implementations of nodes that are widely used. Because the root is stored in memory and generated in the `index.js` file, it was simpler to keep the endpoints there as well. However, if the tree were to be stored in a database, then the code would be refactored to use routes and controllers.

## API Descriptions

### `GET /api/tree` Description
For the implementation of the `GET /api/tree` endpoint and given the TreeNode construction of the tree, I use a helper method `serialize` that takes a given root and recursively reconstructs the tree. Because of the way the id is stored in the object and the desired output, I additionally need the `formatChildren` function to recursively map the `children` of a node to match the required format. This returns a JSON representation of the string that matches the desired output. Requires the root node of the tree.

### `POST /api/tree` Description
For the implementation of the `POST /api/tree` endpoint and given the TreeNode construction of the tree. I use the helper method `findParentAndInsert` to do a preorder traversal of the tree until the parent is found, in which case we insert a new node into the children list with the label provided. This function simply a boolean to indicate if the parent was found and therefore if the provided input was added. Requires the root node of the tree.

## Tests
The tests are outlined in `treeService.test.js` and can be run using
```
npm run test
```