import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

import javafx.application.Application;
import javafx.concurrent.Task;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.layout.*;
import javafx.stage.Stage;

class DateManipulation {

    public static String addDaysToDate(Date date, int daysToAdd) {
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(date);
        calendar.add(Calendar.DATE, daysToAdd);

        SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy");
        return formatter.format(calendar.getTime());
    }
}

class Product {
    private final String id;
    private String name;
    private int quantity;
    private double price;
    private String shipmentMode; // "Land" or "Sea"
    private String type;

    // Constructor
    public Product(String id, String name, int quantity, double price, String shipmentMode) {
        this.id = id;
        this.name = name;
        this.quantity = quantity;
        this.price = price;
        this.shipmentMode = shipmentMode;
        this.type = shipmentMode == "Land" ? "Goods" : "Cargo";
    }

    // Getters and Setters
    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public double getPrice() {
        return price;
    }

    public String getShipmentMode() {
        return shipmentMode;
    }

    public String getType() {
        return type;
    }
}

class Inventory {
    private Product[] products;
    private int size;
    private final int MAX_PRODUCTS = 100;

    public Inventory() {
        products = new Product[MAX_PRODUCTS];
        size = 0;
    }

    // Add product to the inventory
    public synchronized void addProduct(Product product) {
        if (size < MAX_PRODUCTS) {
            int existingIndex = findProductIndex(product.getId());
            if (existingIndex != -1) {
                products[existingIndex] = product;
            } else {
                products[size++] = product;
            }
        }
    }

    // Helper method to find product index by ID
    private int findProductIndex(String productId) {
        for (int i = 0; i < size; i++) {
            if (products[i].getId().equals(productId)) {
                return i;
            }
        }
        return -1;
    }

    // Method to procure product
    public synchronized String procureProduct(String productId, int quantity) {
        int index = findProductIndex(productId);
        if (index == -1) {
            return "Product not found.";
        }

        Product product = products[index];
        if (product.getQuantity() < quantity) {
            return "Product out of stock.";
        }

        product.setQuantity(product.getQuantity() - quantity);
        return "Procured " + quantity + " units of " + product.getId();
    }

    // Generate stock statistics
    public int getTotalInventory() {
        int total = 0;
        for (int i = 0; i < size; i++) {
            total += products[i].getQuantity();
        }
        return total;
    }

    // Get current size of inventory
    public int getSize() {
        return size;
    }

    // Get product by index
    public Product getProduct(int index) {
        if (index >= 0 && index < size) {
            return products[index];
        }
        return null;
    }
}

class Manager {
    private Inventory inventory;

    public Manager(Inventory inventory) {
        this.inventory = inventory;
    }

    public void addProduct(Product product) {
        inventory.addProduct(product);
    }

    public String viewStatistics() {
        String out = "Total Inventory: " + inventory.getTotalInventory() + "\n";

        for (int i = 0; i < inventory.getSize(); i++) {
            Product temp = inventory.getProduct(i);
            out += "\nID: " + temp.getId() + "\nName: " + temp.getName()
                    + "\nQuantity: " + temp.getQuantity() + "\nPrice: " + temp.getPrice()
                    + "\nShipment Mode: " + temp.getShipmentMode() + "\nType: " + temp.getType() + "\n";
        }

        return out;
    }

    public String getLowThresholdString() {
        String out = "";
        for (int i = 0; i < inventory.getSize(); i++) {
            Product temp = inventory.getProduct(i);
            if (temp.getQuantity() < 50) {
                out += "ID: " + temp.getId() + " Name: " + temp.getName() + "\n";
            }
        }
        return out;
    }
}

class Customer {
    private Inventory inventory;

    public Customer(Inventory inventory) {
        this.inventory = inventory;
    }

    public String viewProducts() {
        String out = "";

        for (int i = 0; i < inventory.getSize(); i++) {
            Product temp = inventory.getProduct(i);
            out += "\nID: " + temp.getId() + "\nName: " + temp.getName()
                    + "\nQuantity: " + temp.getQuantity() + "\nPrice: " + temp.getPrice() + "\n";
        }

        return out;
    }

    public void placeOrder(String productId, int quantity) {
        String result = inventory.procureProduct(productId, quantity);
        System.out.println(result);
    }
}

public class IMSv1 extends Application {
    private Inventory inventory = new Inventory();

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Inventory Management System");

        // Manager UI
        VBox managerBox = new VBox(5);
        Label managerLabel = new Label("Manager Panel");

        Alert alert = new Alert(AlertType.INFORMATION);
        alert.setTitle("Information Alert");
        alert.setHeaderText("Low Inventory Warning");
        alert.setContentText("");

        TextField addProductID = new TextField("Product ID");
        TextField addProductName = new TextField("Product Name");
        TextField addProductQuantity = new TextField("Product Quantity");
        TextField addProductPrice = new TextField("Product Price");
        ComboBox<String> shipmentModeComboBox = new ComboBox<>();
        shipmentModeComboBox.getItems().addAll("Land", "Sea");
        shipmentModeComboBox.setValue("Land");

        Button addProductBtn = new Button("Add Product");

        Button viewStatsBtn = new Button("View Statistics");

        Label mgrMsgLabel = new Label();

        managerBox.getChildren().addAll(managerLabel, addProductID, addProductName, addProductQuantity, addProductPrice,
                shipmentModeComboBox,
                addProductBtn, viewStatsBtn, mgrMsgLabel);

        // Customer UI
        VBox customerBox = new VBox(5);
        Label customerLabel = new Label("Customer Panel");

        Button viewProductsBtn = new Button("View Products");
        TextField placeOrderID = new TextField("Product ID");
        TextField placeOrderQuantity = new TextField("Product Quantity");
        Button placeOrderBtn = new Button("Place Order");

        Label cstMsgLabel = new Label();

        customerBox.getChildren().addAll(customerLabel, viewProductsBtn, placeOrderID, placeOrderQuantity,
                placeOrderBtn, cstMsgLabel);

        // Event handlers
        addProductBtn.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent o) {
                Manager manager = new Manager(inventory);
                Product newProduct = new Product(addProductID.getText(), addProductName.getText(),
                        Integer.parseInt(addProductQuantity.getText()), Double.parseDouble(addProductPrice.getText()),
                        shipmentModeComboBox.getValue());

                inventory.addProduct(newProduct);

                mgrMsgLabel.setText("Product added!\nUpdated Inventory:\n" + manager.viewStatistics());
            }
        });

        viewStatsBtn.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent o) {
                Manager manager = new Manager(inventory);
                mgrMsgLabel.setText(manager.viewStatistics());
                if (manager.getLowThresholdString() != "") {
                    alert.setContentText(manager.getLowThresholdString());
                    alert.showAndWait();
                }
            }
        });

        viewProductsBtn.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent o) {
                Customer customer = new Customer(inventory);
                cstMsgLabel.setText(customer.viewProducts());
            }
        });

        placeOrderBtn.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent o) {
                Task<String> placeOrderTask = new Task<>() {
                    @Override
                    protected String call() {
                        Customer customer = new Customer(inventory);
                        customer.placeOrder(placeOrderID.getText(), Integer.parseInt(placeOrderQuantity.getText()));
                        Manager manager = new Manager(inventory);
                        return "Order Placed for Product \nID: " + placeOrderID.getText() + "\nQuantity: "
                                + placeOrderQuantity.getText() + "\nExpected Delivery: "
                                + DateManipulation.addDaysToDate(new Date(), 2) + " ,,, "
                                + "\nReceived Order for \nID: " + placeOrderID.getText() + "\nQuantity: "
                                + placeOrderQuantity.getText() + "\n\nUpdated Inventory: \n" + manager.viewStatistics();
                    }
                };

                placeOrderTask.setOnSucceeded(event -> {
                    Manager manager = new Manager(inventory);

                    System.out.println(placeOrderTask.getValue().split(",,,"));
                    // Run UI updates on the JavaFX Application Thread
                    cstMsgLabel.setText(placeOrderTask.getValue().split(",,,")[0]);
                    mgrMsgLabel.setText(placeOrderTask.getValue().split(",,,")[1]);

                    if (manager.getLowThresholdString() != "") {
                        alert.setContentText(manager.getLowThresholdString());
                        alert.showAndWait();
                    }
                });

                // Start the order placement in a new thread
                new Thread(placeOrderTask).start();
            }
        });

        HBox root = new HBox(20, managerBox, customerBox);
        Scene scene = new Scene(root, 400, 600);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}