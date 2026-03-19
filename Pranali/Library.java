import java.util.*;

class Book {
    String title, author, isbn;

    Book(String t, String a, String i) {
        title = t;
        author = a;
        isbn = i;
    }
}

public class Library {
    ArrayList<Book> list = new ArrayList<>();

    void addBook(Book b) {
        list.add(b);
    }

    void removeBook(String isbn) {
        list.removeIf(b -> b.isbn.equals(isbn));
    }

    void displayBooks() {
        for (Book b : list) {
            System.out.println(b.title + " " + b.author + " " + b.isbn);
        }
    }

    public static void main(String[] args) {
        Library l = new Library();

        // Add books
        l.addBook(new Book("Java", "ABC", "101"));
        l.addBook(new Book("Python", "XYZ", "102"));

        // Display books
        System.out.println("Books in Library:");
        l.displayBooks();

        // Remove book
        l.removeBook("101");

        System.out.println("\nAfter Removing:");
        l.displayBooks();
    }
}