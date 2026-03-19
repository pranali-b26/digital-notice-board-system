class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    void display() {
        System.out.println(name + " " + age);
    }

    public static void main(String[] args) {
        Person p1 = new Person("Aman", 20);
        Person p2 = new Person("Riya", 22);

        p1.display();
        p2.display();
    }
}