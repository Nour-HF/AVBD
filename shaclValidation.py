from pyshacl import validate

data_file = "knowledgeGraph.ttl"
shapes_file = "constraints.ttl"

# Run the validation
r = validate(
    data_file,
    shacl_graph=shapes_file,
    ont_graph=None,
    inference='rdfs',
    abort_on_first=False,
    meta_shacl=False,
    debug=False
)

conforms, results_graph, results_text = r

# Print the validation results
print("Conforms:", conforms)
print(results_text)