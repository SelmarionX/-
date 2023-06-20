package lesson3;

public class main {
    public static void main(String[] args) {
        System.out.println("ОДНОСВЯЗНЫЙ СПИСОК");
        System.out.println("-------------------");
        SingleLinkedList list = new SingleLinkedList();
        System.out.println("Добавление в начало списка:");
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.print();
        System.out.println("-------------------");
        System.out.println("Удаление из начала списка:");
        list.removeFirst();
        list.print();
        System.out.println("-------------------");
        System.out.println("Добавление в конец списка:");
        list.addLast(4);
        list.addLast(5);
        list.print();
        System.out.println("-------------------");
        System.out.println("Удаление из конца списка:");
        list.removeLast();
        list.print();
        System.out.println("-------------------");
        System.out.println("Разворот односвязанного списка:");
        list.revert();
        list.print();
        System.out.println("-------------------");
        System.out.println("Проверка на наличие значения в списке:");
        System.out.println("Содержится ли число 4 в списке: " + list.contains(4));
        System.out.println("Содержится ли число 5 в списке: " + list.contains(5));
        System.out.println("-------------------");
        System.out.println("Очистка списка:");
        list.clearList();
        list.print();
        System.out.println("-------------------");
    }
}