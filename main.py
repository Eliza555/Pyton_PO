class Table:
    """Класс, описывающий простой стол."""

    def __init__(self, material, length, width):
        self.material = material
        self.length = length
        self.width = width

    def resize(self, new_length, new_width):
        """Изменяет размеры стола."""
        self.length = new_length
        self.width = new_width

    def clean(self):
        """Очищает стол."""
        print("Стол очищен.")


class Tree:
    """Класс, описывающий простое дерево."""

    def __init__(self, species, height, age):
        self.species = species
        self.height = height
        self.age = age

    def grow(self, amount):
        """Увеличивает высоту дерева."""
        self.height += amount
        print(f"Дерево выросло на {amount} метров.")

    def shed_leaves(self):
        """Имитирует листопад."""
        print("Листья опали.")


class Facebook:
    """Класс, описывающий простую социальную сеть Facebook."""

    def __init__(self, user_count, trending_topics):
        self.user_count = user_count
        self.trending_topics = trending_topics

    def post_update(self, content):
        """Публикует обновление статуса."""
        print(f"Обновление статуса: {content}")

    def add_trending_topic(self, topic):
        """Добавляет новую тему в тренды."""
        self.trending_topics.append(topic)
        print(f"Добавлена новая трендовая тема: {topic}")


# Примеры использования
if __name__ == "__main__":
    # Пример работы с классом Table
    table = Table("дерево", 120.5, 60.0)
    print(f"Материал стола: {table.material}")
    table.resize(130.0, 65.0)
    print(f"Новые размеры стола: {table.length} см x {table.width} см")
    table.clean()

    print("\n-----------------\n")

    # Пример работы с классом Tree
    tree = Tree("Ясень", 5.5, 10)
    print(f"Вид дерева: {tree.species}")
    tree.grow(0.5)
    print(f"Новая высота дерева: {tree.height} метров")
    tree.shed_leaves()

    print("\n-----------------\n")

    # Пример работы с классом Facebook
    fb = Facebook(1000000, ["Python", "AI"])
    print(f"Количество пользователей: {fb.user_count}")
    print(f"Трендовые темы: {fb.trending_topics}")
    fb.post_update("Hello, world!")
    fb.add_trending_topic("OpenAI")
    print(f"Обновлённые трендовые темы: {fb.trending_topics}")