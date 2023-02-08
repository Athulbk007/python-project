def file_read(fna):
    with open(fna) as f:
        output_list=f.readlines()
    print(output_list)
file_read('text.txt')