import javafx.application.*;
import javafx.stage.*;
import javafx.scene.*;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.scene.paint.*;
import javafx.scene.canvas.*;
import javafx.scene.shape.*;
import javafx.scene.text.*;
import javafx.event.*;
import javafx.geometry.*;
import javafx.collections.*;

public class StudentRegForm extends Application {
  String genderString = "";
  String departmentString = "";

  public static void main(String[] args) {
    launch(args);
  }
  public void start(Stage stage) {
    FlowPane root = new FlowPane(10, 10);
    Scene scene = new Scene(root, 400, 300);
    Label namelbl = new Label("Name:");
    Label reglbl = new Label("Registration Number:");
    TextField nametf = new TextField();
    TextField regtf = new TextField();
    Label genderlbl = new Label("Gender:");
    RadioButton male = new RadioButton("Male");
    male.setOnAction((ae)-> {genderString = "Male";});
    RadioButton female = new RadioButton("Female");
    female.setOnAction((ae)-> {genderString = "Female";});
    ToggleGroup gender = new ToggleGroup();
    male.setToggleGroup(gender);
    female.setToggleGroup(gender);
    male.fire();
    CheckBox cbox = new CheckBox("Department");
    Button display = new Button("Display");
    ObservableList<String> dpts =  FXCollections.observableArrayList("Computer Science", "Information Technology", "Electronics", "Mechanical", "Civil");
    ComboBox<String> combox = new ComboBox<String>(dpts);
    Canvas canvas = new Canvas(400, 300);
    GraphicsContext gc = canvas.getGraphicsContext2D();
    gc.setFill(Color.RED);
    gc.strokeRect(0, 0, 400, 300);
    gc.fillRect(0, 0, 400, 300);
    gc.setFill(Color.WHITE);
    gc.fillRect(0, 0, 300, 300);
    gc.strokeOval(100, 100, 100, 100);
    gc.setFill(Color.BLACK);
    gc.fillText("Hello", 100, 100);
    gc.strokeLine(0, 0, 300, 300);
    display.setOnAction(new EventHandler<ActionEvent>() {
      public void handle(ActionEvent e) {
        System.out.println("Name: " + nametf.getText());
        System.out.println("Registration Number: " + regtf.getText());
        System.out.println("Gender: " + genderString);
        System.out.println("Department: " + combox.getValue());
        System.out.println("Department: " + cbox.isSelected());
      }
    });
    root.getChildren().addAll(namelbl, nametf, reglbl, regtf, genderlbl, male, female, cbox, combox, display, canvas);
    stage.setScene(scene);
    stage.setTitle("Student Registration Form");
    stage.show();
  }
}