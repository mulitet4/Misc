import javafx.application.*;
import javafx.stage.*;
import javafx.scene.*;
import javafx.scene.layout.*;
import javafx.scene.control.*;
import javafx.geometry.*;
import javafx.event.*;

class JavafxDemo extends Application{
  public void init(){}
  public void start(Stage ps){
    FlowPane root = new FlowPane(10, 10);
    root.setAlignment(Pos.TOP_CENTER);
    Scene sc = new Scene(root, 300, 300);
    Label lblhi = new Label("hello");
    TextField tf1 = new TextField();
    Button btndone = new Button("Done");

    btndone.setOnAction(new EventHandler<ActionEvent>(){
      public void handle(ActionEvent o){
        lblhi.setText(tf1.getText());
      }
    });

    root.getChildren().addAll(lblhi, tf1, btndone);
    ps.setScene(sc);
    ps.setTitle("First Program");
    ps.show();
  }
  public static void main(String[] args){
    launch
  }
}