import javafx.application.Application;
import javafx.application.Platform;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Button;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ToggleGroup;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class TextScrollingApp extends Application {

  private boolean scrolling = false; // To control the scrolling thread
  private double xPosition = 400; // Initial x position of the text
  private String direction = "Left"; // Initial direction (default is "Left")

  @Override
  public void start(Stage primaryStage) {
    // Create the canvas for drawing the message
    Canvas canvas = new Canvas(400, 100);
    GraphicsContext gc = canvas.getGraphicsContext2D();

    // Create RadioButtons for direction selection
    RadioButton leftToRight = new RadioButton("Left to Right");
    RadioButton rightToLeft = new RadioButton("Right to Left");
    ToggleGroup directionGroup = new ToggleGroup();
    leftToRight.setToggleGroup(directionGroup);
    rightToLeft.setToggleGroup(directionGroup);
    rightToLeft.setSelected(true); // Default selection

    // Create buttons for starting and stopping the scrolling
    Button startButton = new Button("Start");
    Button stopButton = new Button("Stop");

    // Set up RadioButton actions to change scrolling direction
    leftToRight.setOnAction(e -> direction = "Right");
    rightToLeft.setOnAction(e -> direction = "Left");

    // Set up the Start button to initiate scrolling
    startButton.setOnAction(e -> {
      if (!scrolling) {
        scrolling = true;
        new Thread(() -> scrollMessage(gc, canvas.getWidth())).start();
      }
    });

    // Set up the Stop button to halt scrolling
    stopButton.setOnAction(e -> scrolling = false);

    // Layout arrangement
    HBox directionBox = new HBox(10, leftToRight, rightToLeft);
    VBox root = new VBox(10, canvas, directionBox, new HBox(10, startButton, stopButton));
    root.setPadding(new Insets(15));

    // Configure the primary stage (window)
    Scene scene = new Scene(root, 450, 200);
    primaryStage.setTitle("Simple Message Scroller");
    primaryStage.setScene(scene);
    primaryStage.show();
  }

  private void scrollMessage(GraphicsContext gc, double canvasWidth) {
    String message = "Scrolling Message";

    while (scrolling) {
      // Clear the canvas before drawing
      Platform.runLater(() -> {
        gc.clearRect(0, 0, canvasWidth, 100);
        gc.fillText(message, xPosition, 50);
      });

      // Update the x position based on the direction
      if ("Left".equals(direction)) {
        xPosition -= 2; // Move left
        if (xPosition < -100) { // Reset when message goes out of bounds (approximate length)
          xPosition = canvasWidth;
        }
      } else {
        xPosition += 2; // Move right
        if (xPosition > canvasWidth) { // Reset when message goes out of bounds
          xPosition = -100; // Reset position to start from the left
        }
      }

      // Control the speed of the scrolling
      try {
        Thread.sleep(30);
      } catch (InterruptedException ex) {
        Thread.currentThread().interrupt();
      }
    }
  }

  public static void main(String[] args) {
    launch(args);
  }
}
