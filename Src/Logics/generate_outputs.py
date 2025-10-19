import os
from Src.Logics.factory_entities import factory_entities
from Src.Logics.start_factory import start_factory

def main():
    #получаем данные
    factory_data = start_factory()
    all_data = factory_data.get_all()

    #создаём фабрику
    factory = factory_entities()
    # форматы
    formats = ["csv", "markdown", "json", "xml"]
    # Папка для сохранения
    output_dir = os.path.join(os.getcwd(), "Output")
    os.makedirs(output_dir, exist_ok=True)
    # Генерация
    for fmt in formats:
        try:
            response = factory.create(fmt)
            for name, dataset in all_data.items():
                text = response.build(fmt, dataset)
                file_path = os.path.join(output_dir, f"{name}.{fmt}")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(text)

                print(f"[OK] {name} -> {file_path}")

        except Exception as e:
            print(f"[ERROR] Не удалось создать {fmt}: {e}")

    print("Генерация файлов завершена")


if __name__ == "__main__":
    main()
