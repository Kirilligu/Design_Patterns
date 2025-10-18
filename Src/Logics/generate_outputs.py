import os
from dataclasses import dataclass
from Src.Logics.factory_entities import factory_entities
@dataclass
class TestItem:
    name: str
    value: int

def main():
    data = [
        TestItem("Item1", 100),
        TestItem("Item2", 200),
        TestItem("Item3", 300)
    ]

    #создаём фабрику
    factory = factory_entities()

    # форматы
    formats = ["csv", "markdown", "json", "xml"]

    # Папка вырузки
    output_dir = os.path.join(os.getcwd(), "Output")
    os.makedirs(output_dir, exist_ok=True)

    # генерация файлов для каждого формата
    for fmt in formats:
        try:
            response = factory.create(fmt)
            text = response.build(fmt, data)
            file_path = os.path.join(output_dir, f"sample.{fmt}")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"[OK] Файл успешно создан: {file_path}")
        except Exception as e:
            print(f"[ERROR] Не удалось создать файл для формата {fmt}: {e}")

    print("Генерация файлов завершена.")

if __name__ == "__main__":
    main()
