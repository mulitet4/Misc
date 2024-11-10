import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.ListView;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;
import java.util.HashMap;
import java.util.Map;

public class StudentDetailsApp extends Application {

  // Example student data (assuming earlier labs created similar data)
  private final Map<String, Student> studentData = new HashMap<>();

  @Override
  public void start(Stage primaryStage) {
    // Initialize some example student data
    initializeStudentData();

    // ListView for selecting student register numbers
    ListView<String> listView = new ListView<>();
    listView.getItems().addAll(studentData.keySet()); // Populate with student register numbers

    // Canvas to display selected student details
    Canvas canvas = new Canvas(400, 200);
    GraphicsContext gc = canvas.getGraphicsContext2D();

    // Event listener for ListView selection
    listView.getSelectionModel().selectedItemProperty().addListener((observable, oldValue, newValue) -> {
      if (newValue != null) {
        displayStudentDetails(gc, studentData.get(newValue));
      }
    });

    // Layout arrangement
    HBox root = new HBox(10, listView, canvas);
    Scene scene = new Scene(root, 600, 250);

    // Configure the Stage (Window)
    primaryStage.setTitle("Student Details Viewer");
    primaryStage.setScene(scene);
    primaryStage.show();
  }

  // Method to display student details on the canvas
  private void displayStudentDetails(GraphicsContext gc, Student student) {
    // Clear the previous content
    gc.clearRect(0, 0, 400, 200);

    // Display student details
    gc.fillText("Student Details", 10, 20);
    gc.fillText("Registration No: " + student.getRegisterNumber(), 10, 50);
    gc.fillText("Name: " + student.getName(), 10, 80);
    gc.fillText("Age: " + student.getAge(), 10, 110);
    gc.fillText("Course: " + student.getCourse(), 10, 140);
  }

  // Initialize example student data
  private void initializeStudentData() {
    studentData.put("230962162", new Student("230962162", "Aaryan Dongre", 19, "CSE AI/ML"));
    studentData.put("230962163", new Student("230962163", "Rajesh Sharma", 19, "CSE AI/ML"));
    studentData.put("230962165", new Student("230962165", "Puneet Singh", 19, "CSE AI/ML"));
  }

  // Inner class to represent a Student
  class Student {
    private final String registerNumber;
    private final String name;
    private final int age;
    private final String course;

    public Student(String registerNumber, String name, int age, String course) {
      this.registerNumber = registerNumber;
      this.name = name;
      this.age = age;
      this.course = course;
    }

    public String getRegisterNumber() {
      return registerNumber;
    }

    public String getName() {
      return name;
    }

    public int getAge() {
      return age;
    }

    public String getCourse() {
      return course;
    }
  }

  public static void main(String[] args) {
    launch(args);
  }
}
