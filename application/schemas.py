schema = {
"type": "object",
"properties": {
    "name": {
    "type": "string"
    },
    "description": {
    "type": "string"
    },
    "completed": {
    "type": "string"
    },
    "date_created": {
    "type": "string",
    }
},
"required": [
    "name",
    "description",
    "completed"
],
"optional": [
    "documents"
]
}