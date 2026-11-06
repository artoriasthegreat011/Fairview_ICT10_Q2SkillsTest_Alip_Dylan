from pyscript import document
# something
# something AGAIN
nonmetal = {
    'H' : ('Hydrogen', 1, 1.008),
    'He' : ('Helium', 2, 4.0026),
    'C' : ('Carbon', 6, 12.011),
    'N' : ('Nitrogen', 7, 14.007),
    'O' : ('Oxygen', 8, 15.999),
    'F' : ('Fluorine', 9, 18.998),
    'Ne' : ('Neon', 10, 20.180),
    'P' : ('Phosphorus', 15, 30.974),
    'S' : ('Sulfur', 16, 32.07),
    'Cl' : ('Chlorine', 17, 35.45),
    'Ar' : ('Argon', 18, 39.9),
    'Se' : ('Selenium', 34, 78.971),
    'Br' : ('Bromine', 35, 79.904),
    'Kr' : ('Krypton', 36, 83.798),
    'I' : ('Iodine', 53, 126.905),
    'Xe' : ('Xenon', 54, 131.293),
    'At' : ('Astatine', 85, 210),
    'Rn' : ('Radon', 86, 222),
    'Ts' : ('Tennessine', 117, 294),
    'Og' : ('Oganesson', 118, 294)
    }

# function to search for nonmetals
def search_nonmetal(e):
    # get the input from the html file

    nonmetal_1 = document.getElementById("nonmetal1").value
    # retrieve information from the dictionary
    result = nonmetal.get(nonmetal_1, ('Nonmetal not found', '-', '-'))
    # display the result in html
    document.getElementById("symbol").innerText = nonmetal_1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]