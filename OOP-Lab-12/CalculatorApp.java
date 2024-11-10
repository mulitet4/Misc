import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.event.*;

public class CalculatorApp extends Application {

  @Override
  public void start(Stage primaryStage) {
    // Creating input fields
    TextField numberField1 = new TextField();
    TextField numberField2 = new TextField();
    numberField1.setPromptText("Enter first number");
    numberField2.setPromptText("Enter second number");

    // Creating Canvas for displaying results
    Canvas canvas = new Canvas(300, 150); // Width: 300px, Height: 150px
    GraphicsContext gc = canvas.getGraphicsContext2D();

    // Creating the Compute Button with a calculator image
    Button computeButton = new Button("Compute");
    Image calculatorImage = new Image("Calculator.jpg"); // Ensure "calculator.png" is in your resources
    computeButton.setGraphic(new javafx.scene.image.ImageView(calculatorImage));

    // Set up button click event
    computeButton.setOnAction(new EventHandler<ActionEvent>() {
      public void handle(ActionEvent e) {
        try {
          // Parsing the input values
          double num1 = Double.parseDouble(numberField1.getText());
          double num2 = Double.parseDouble(numberField2.getText());

          // Performing calculations
          double sum = num1 + num2;
          double product = num1 * num2;
          double difference = num1 - num2;
          double quotient = num2 != 0 ? num1 / num2 : Double.NaN;

          // Clearing and displaying results on the canvas
          gc.clearRect(0, 0, canvas.getWidth(), canvas.getHeight());
          gc.fillText("Sum: " + sum, 10, 20);
          gc.fillText("Product: " + product, 10, 40);
          gc.fillText("Difference: " + difference, 10, 60);
          gc.fillText("Quotient: " + (num2 != 0 ? quotient : "Undefined (Division by 0)"), 10, 80);

        } catch (NumberFormatException ex) {
          gc.clearRect(0, 0, canvas.getWidth(), canvas.getHeight());
          gc.fillText("Invalid input. Please enter valid numbers.", 10, 20);
        }

      }
    }

    );

    // Arranging components in a layout
    VBox root = new VBox(10, numberField1, numberField2, computeButton, canvas);
    root.setPadding(new Insets(15));

    // Setting up the Stage (Window)
    Scene scene = new Scene(root, 400, 300);
    primaryStage.setTitle("JavaFX Calculator");
    primaryStage.setScene(scene);
    primaryStage.show();
  }

  public static void main(String[] args) {
    launch(args);
  }
}
