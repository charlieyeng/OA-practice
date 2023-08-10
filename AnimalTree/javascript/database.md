## Task 3: Database Schema
Given the TreeNode class that I used for this exercise, I would create a DB schema for the TreeNode. It would have the fields `id` as the unique identifer and the fields `label` and `children`. An additional `createdAt` field should also be added to track creation times.
| `id`      | `label`             | `children` | `createdAt` |
| ----------- | --------------------- | --------------- | ----------- |
| uuid | string | Array<TreeNode>| date |

## Task 4: Sample Queries
This exercise was tested in Postman.

For the `GET /api/tree endpoint`, a `GET` request to `localhost:3001/api/tree` with no body will fetch the tree stored in memory.

For the `POST /api/tree endpoint`, a `POST` request to `localhost:3001/api/tree` with a body of
```
{
    "parent": "<id>",
    "label": "<label>"
}
```
will cause a node to be added the end of the children with a random uuid generated. We generate the uuid randomly to ensure unique identifiers with a well known library.

Example Body:
```
{
    "parent": "1",
    "label": "monkey"
}
```
The subsequent tree can be verified using a `GET /api/tree endpoint` call.
