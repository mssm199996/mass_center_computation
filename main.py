import math

def main():
    density = 1.91
    file_names = ['source_1.csv', 'source_2.csv', 'source_3.csv', 'source_4.csv']

    for file_name in file_names:
        treat_file('sources/' + file_name, density)


def treat_file(filename, density):
    # Opening a specific file to treat it
    file = open(filename, 'r')
    Lines = file.readlines()

    current_line_index = 0

    mass_sum = 0.0 # Sum of M(i)
    z_mass_sum = 0.0 # Sum of M(i) * Z(i)

    for line in Lines:
        current_line_index += 1

        # Skiping the first 8 lines (0 is involved)
        if (current_line_index > 9):
            # Removing line feeds and converting the line to a vector
            atom_details = line.replace('\n', '').split(' ')

            z = float(atom_details[3])
            diameter = float(atom_details[4])

            atom_mass = (4/3) * (math.pi) * math.pow(diameter, 3) * density
            atom_z_mass = z * atom_mass

            mass_sum += atom_mass
            z_mass_sum += atom_z_mass

    mass_center = z_mass_sum / mass_sum

    file.close()

    print(filename + " => " + str(mass_sum))

main()
