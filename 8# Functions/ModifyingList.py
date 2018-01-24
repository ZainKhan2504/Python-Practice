unprinted_design = ['iphone case','robot pendant','dodecahedron']
complete_model = []

def printmodel(unprinted_design, complete_model):
    while unprinted_design:
        design = unprinted_design.pop()
        print("Printing model: "+design)
        complete_model.append(design)

def show_complete_model(complete_model):
    for complete_model in complete_model:
        print(complete_model)

printmodel(unprinted_design,complete_model)
show_complete_model(complete_model)