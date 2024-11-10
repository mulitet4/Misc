import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class ResumeApp extends Application {

  @Override
  public void start(Stage primaryStage) {
    // Text fields for user input
    TextField nameField = new TextField();
    TextField emailField = new TextField();
    TextField phoneField = new TextField();
    TextField addressField = new TextField();
    nameField.setPromptText("Enter your name");
    emailField.setPromptText("Enter your email");
    phoneField.setPromptText("Enter your phone number");
    addressField.setPromptText("Enter your address");

    // Checkboxes for languages
    CheckBox langEnglish = new CheckBox("English");
    CheckBox langSpanish = new CheckBox("Spanish");
    CheckBox langFrench = new CheckBox("French");
    CheckBox langGerman = new CheckBox("German");
    CheckBox langChinese = new CheckBox("Chinese");

    // Creating the Canvas for displaying the resume
    Canvas canvas = new Canvas(400, 300);
    GraphicsContext gc = canvas.getGraphicsContext2D();

    // Button to submit and display resume
    Button submitButton = new Button("Submit");

    // Event handler for button click
    submitButton.setOnAction(e -> {
      // Retrieve input values
      String name = nameField.getText();
      String email = emailField.getText();
      String phone = phoneField.getText();
      String address = addressField.getText();

      // Build a list of selected languages
      StringBuilder languages = new StringBuilder();
      if (langEnglish.isSelected())
        languages.append("English ");
      if (langSpanish.isSelected())
        languages.append("Spanish ");
      if (langFrench.isSelected())
        languages.append("French ");
      if (langGerman.isSelected())
        languages.append("German ");
      if (langChinese.isSelected())
        languages.append("Chinese ");

      // Clear the Canvas before rendering new details
      gc.clearRect(0, 0, canvas.getWidth(), canvas.getHeight());

      // Display resume details
      gc.fillText("Resume", 10, 20);
      gc.fillText("Name: " + name, 10, 40);
      gc.fillText("Email: " + email, 10, 60);
      gc.fillText("Phone: " + phone, 10, 80);
      gc.fillText("Address: " + address, 10, 100);
      gc.fillText("Languages Spoken: " + (languages.length() > 0 ? languages.toString() : "None"), 10, 120);
    });

    // Arranging components in a layout
    VBox root = new VBox(10, nameField, emailField, phoneField, addressField,
        langEnglish, langSpanish, langFrench, langGerman, langChinese,
        submitButton, canvas);
    root.setPadding(new Insets(15));

    // Setting up the Stage (Window)
    Scene scene = new Scene(root, 500, 500);
    primaryStage.setTitle("Resume Builder");
    primaryStage.setScene(scene);
    primaryStage.show();
  }

  public static void main(String[] args) {
    launch(args);
  }
}
