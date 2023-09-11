import os
from pyment import PyComment

filename = 'hyperparam_space.py'

if os.path.exists(filename):
    c = PyComment(filename)
    c.proceed()

    # Получаем вывод и сохраняем его в файл
    output_docs = c.get_output_docs()
    with open(os.path.basename(filename) + ".patch", "w") as f:
        for s in output_docs:
            f.write(s + "\n")

    # Выводим результаты на экран
    for s in output_docs:
        print(s)
else:
    print(f"Файл '{filename}' не найден.")