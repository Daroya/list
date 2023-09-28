folder_path = "Путь к файлу"
file_name = input("Напишіть зразу назву словника: ")  

file_path = folder_path + "\\" + file_name

text = input('Тепер напиши текст який буде в списку:')

with open(file_path, "w+") as my_file:
    my_file.write(text) 
