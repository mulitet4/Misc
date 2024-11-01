import javafx.application.Application;
import javafx.beans.property.SimpleStringProperty;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.*;
import javafx.stage.Stage;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.ConcurrentHashMap;

abstract class Product {
  private String id;
  private String name;
  private double price;
  private int quantity;
  private int minStockLimit;

  public Product(String id, String name, double price, int quantity, int minStockLimit) {
      this.id = id;
      this.name = name;
      this.price = price;
      this.quantity = quantity;
      this.minStockLimit = minStockLimit;
  }

  // Getters and setters
  public String getId() { return id; }
  public String getName() { return name; }
  public double getPrice() { return price; }
  public int getQuantity() { return quantity; }
  public int getMinStockLimit() { return minStockLimit; }

  public void setQuantity(int quantity) {
      this.quantity = quantity;
  }

  public abstract String getShipmentMode();
  public abstract int getDeliveryDays();
}

// Good.java
class Good extends Product {
  public Good(String id, String name, double price, int quantity, int minStockLimit) {
      super(id, name, price, quantity, minStockLimit);
  }

  @Override
  public String getShipmentMode() {
      return "Land";
  }

  @Override
  public int getDeliveryDays() {
      return 3; // Standard delivery time for land shipment
  }
}

// Cargo.java
class Cargo extends Product {
  public Cargo(String id, String name, double price, int quantity, int minStockLimit) {
      super(id, name, price, quantity, minStockLimit);
  }

  @Override
  public String getShipmentMode() {
      return "Sea";
  }

  @Override
  public int getDeliveryDays() {
      return 14; // Standard delivery time for sea shipment
  }
}

// Order.java
class Order {
  private String orderId;
  private String productId;
  private int quantity;
  private String location;
  private LocalDateTime orderDate;

  public Order(String orderId, String productId, int quantity, String location) {
      this.orderId = orderId;
      this.productId = productId;
      this.quantity = quantity;
      this.location = location;
      this.orderDate = LocalDateTime.now();
  }

  // Getters
  public String getOrderId() { return orderId; }
  public String getProductId() { return productId; }
  public int getQuantity() { return quantity; }
  public String getLocation() { return location; }
  public LocalDateTime getOrderDate() { return orderDate; }
}

// InventorySystem.java
class InventorySystem {
  private Map<String, Product> products = new ConcurrentHashMap<>();
  private List<Order> orders = Collections.synchronizedList(new ArrayList<>());
  private List<String> notifications = Collections.synchronizedList(new ArrayList<>());

  public synchronized boolean addProduct(Product product) {
      if (products.containsKey(product.getId())) {
          return false;
      }
      products.put(product.getId(), product);
      return true;
  }

  public synchronized boolean procureProduct(String productId, int quantity, String location) {
      Product product = products.get(productId);
      if (product == null || product.getQuantity() < quantity) {
          return false;
      }

      product.setQuantity(product.getQuantity() - quantity);
      orders.add(new Order(UUID.randomUUID().toString(), productId, quantity, location));

      if (product.getQuantity() < product.getMinStockLimit()) {
          notifications.add("Low stock alert for product: " + product.getName());
      }

      return true;
  }

  public List<Product> getAllProducts() {
      return new ArrayList<>(products.values());
  }

  public List<String> getNotifications() {
      return new ArrayList<>(notifications);
  }

  public Map<String, Integer> getOrdersByLocation() {
      Map<String, Integer> ordersByLocation = new HashMap<>();
      for (Order order : orders) {
          ordersByLocation.merge(order.getLocation(), order.getQuantity(), Integer::sum);
      }
      return ordersByLocation;
  }

  public int getTotalRemainingProducts(String type) {
      return products.values().stream()
              .filter(p -> (type.equals("Good") && p instanceof Good) ||
                         (type.equals("Cargo") && p instanceof Cargo))
              .mapToInt(Product::getQuantity)
              .sum();
  }

  public int getOrdersInPeriod(LocalDateTime start, LocalDateTime end) {
      return (int) orders.stream()
              .filter(o -> !o.getOrderDate().isBefore(start) && !o.getOrderDate().isAfter(end))
              .count();
  }
}

public class IMSv3 extends Application {
  private InventorySystem inventorySystem = new InventorySystem();
  private boolean isManager = false;

  @Override
  public void start(Stage primaryStage) {
      primaryStage.setTitle("Inventory Management System");

      // Login Scene
      VBox loginLayout = new VBox(10);
      loginLayout.setPadding(new Insets(10));
      
      Button managerLoginBtn = new Button("Login as Manager");
      Button customerLoginBtn = new Button("Login as Customer");
      
      loginLayout.getChildren().addAll(managerLoginBtn, customerLoginBtn);
      Scene loginScene = new Scene(loginLayout, 300, 200);

      // Main Layout
      VBox mainLayout = new VBox(10);
      mainLayout.setPadding(new Insets(10));

      // Product List
      TableView<Product> productTable = new TableView<>();
      TableColumn<Product, String> idCol = new TableColumn<>("ID");
      TableColumn<Product, String> nameCol = new TableColumn<>("Name");
      TableColumn<Product, Double> priceCol = new TableColumn<>("Price");
      TableColumn<Product, Integer> quantityCol = new TableColumn<>("Quantity");
      TableColumn<Product, String> shipmentCol = new TableColumn<>("Shipment Mode");

      idCol.setCellValueFactory(new PropertyValueFactory<>("id"));
      nameCol.setCellValueFactory(new PropertyValueFactory<>("name"));
      priceCol.setCellValueFactory(new PropertyValueFactory<>("price"));
      quantityCol.setCellValueFactory(new PropertyValueFactory<>("quantity"));
      shipmentCol.setCellValueFactory(cellData -> 
          new SimpleStringProperty(cellData.getValue().getShipmentMode()));

      productTable.getColumns().addAll(idCol, nameCol, priceCol, quantityCol, shipmentCol);

      // Add Product Form (only visible to manager)
      GridPane addProductForm = new GridPane();
      addProductForm.setHgap(10);
      addProductForm.setVgap(10);
      addProductForm.setVisible(false);

      TextField idField = new TextField();
      TextField nameField = new TextField();
      TextField priceField = new TextField();
      TextField quantityField = new TextField();
      TextField minStockField = new TextField();
      ComboBox<String> typeComboBox = new ComboBox<>();
      typeComboBox.getItems().addAll("Good", "Cargo");

      addProductForm.addRow(0, new Label("ID:"), idField);
      addProductForm.addRow(1, new Label("Name:"), nameField);
      addProductForm.addRow(2, new Label("Price:"), priceField);
      addProductForm.addRow(3, new Label("Quantity:"), quantityField);
      addProductForm.addRow(4, new Label("Min Stock:"), minStockField);
      addProductForm.addRow(5, new Label("Type:"), typeComboBox);

      Button addProductBtn = new Button("Add Product");
      addProductForm.addRow(6, addProductBtn);

      // Purchase Form (only visible to customer)
      GridPane purchaseForm = new GridPane();
      purchaseForm.setHgap(10);
      purchaseForm.setVgap(10);
      purchaseForm.setVisible(false);

      TextField purchaseIdField = new TextField();
      TextField purchaseQuantityField = new TextField();
      TextField locationField = new TextField();

      purchaseForm.addRow(0, new Label("Product ID:"), purchaseIdField);
      purchaseForm.addRow(1, new Label("Quantity:"), purchaseQuantityField);
      purchaseForm.addRow(2, new Label("Location:"), locationField);

      Button purchaseBtn = new Button("Purchase");
      purchaseForm.addRow(3, purchaseBtn);

      // Statistics Area (only visible to manager)
      VBox statsArea = new VBox(10);
      statsArea.setVisible(false);
      
      Button viewStatsBtn = new Button("View Statistics");
      TextArea statsText = new TextArea();
      statsText.setEditable(false);
      statsArea.getChildren().addAll(viewStatsBtn, statsText);

      mainLayout.getChildren().addAll(productTable, addProductForm, purchaseForm, statsArea);
      Scene mainScene = new Scene(mainLayout, 800, 600);

      // Event Handlers
      managerLoginBtn.setOnAction(e -> {
          isManager = true;
          addProductForm.setVisible(true);
          statsArea.setVisible(true);
          purchaseForm.setVisible(false);
          primaryStage.setScene(mainScene);
          refreshProductTable(productTable);
      });

      customerLoginBtn.setOnAction(e -> {
          isManager = false;
          addProductForm.setVisible(false);
          statsArea.setVisible(false);
          purchaseForm.setVisible(true);
          primaryStage.setScene(mainScene);
          refreshProductTable(productTable);
      });

      addProductBtn.setOnAction(e -> {
          try {
              Product product;
              if (typeComboBox.getValue().equals("Good")) {
                  product = new Good(
                      idField.getText(),
                      nameField.getText(),
                      Double.parseDouble(priceField.getText()),
                      Integer.parseInt(quantityField.getText()),
                      Integer.parseInt(minStockField.getText())
                  );
              } else {
                  product = new Cargo(
                      idField.getText(),
                      nameField.getText(),
                      Double.parseDouble(priceField.getText()),
                      Integer.parseInt(quantityField.getText()),
                      Integer.parseInt(minStockField.getText())
                  );
              }

              if (inventorySystem.addProduct(product)) {
                  showAlert(Alert.AlertType.INFORMATION, "Success", "Product added successfully");
                  refreshProductTable(productTable);
              } else {
                  showAlert(Alert.AlertType.ERROR, "Error", "Product ID already exists");
              }
          } catch (NumberFormatException ex) {
              showAlert(Alert.AlertType.ERROR, "Error", "Invalid input values");
          }
      });

      purchaseBtn.setOnAction(e -> {
          try {
              String productId = purchaseIdField.getText();
              int quantity = Integer.parseInt(purchaseQuantityField.getText());
              String location = locationField.getText();

              if (inventorySystem.procureProduct(productId, quantity, location)) {
                  Product product = inventorySystem.getAllProducts().stream()
                      .filter(p -> p.getId().equals(productId))
                      .findFirst()
                      .orElse(null);

                  if (product != null) {
                      String confirmationMessage = String.format(
                          "Order Confirmation\n\nProduct: %s\nQuantity: %d\nTotal Amount: $%.2f\n" +
                          "Shipment Mode: %s\nExpected Delivery: %d days",
                          product.getName(), quantity, product.getPrice() * quantity,
                          product.getShipmentMode(), product.getDeliveryDays()
                      );
                      showAlert(Alert.AlertType.INFORMATION, "Order Confirmation", confirmationMessage);
                      refreshProductTable(productTable);
                  }
              } else {
                  showAlert(Alert.AlertType.ERROR, "Error", "Product not available or insufficient stock");
              }
          } catch (NumberFormatException ex) {
              showAlert(Alert.AlertType.ERROR, "Error", "Invalid quantity");
          }
      });

      viewStatsBtn.setOnAction(e -> {
          Map<String, Integer> ordersByLocation = inventorySystem.getOrdersByLocation();
          int totalGoods = inventorySystem.getTotalRemainingProducts("Good");
          int totalCargo = inventorySystem.getTotalRemainingProducts("Cargo");
          
          StringBuilder stats = new StringBuilder();
          stats.append("Statistics:\n\n");
          stats.append("Orders by Location:\n");
          ordersByLocation.forEach((loc, count) -> 
              stats.append(String.format("%s: %d orders\n", loc, count)));
          stats.append("\nRemaining Products:\n");
          stats.append(String.format("Goods: %d\n", totalGoods));
          stats.append(String.format("Cargo: %d\n", totalCargo));

          statsText.setText(stats.toString());
      });

      primaryStage.setScene(loginScene);
      primaryStage.show();
  }

  private void refreshProductTable(TableView<Product> table) {
      table.getItems().clear();
      table.getItems().addAll(inventorySystem.getAllProducts());
  }

  private void showAlert(Alert.AlertType type, String title, String content) {
      Alert alert = new Alert(type);
      alert.setTitle(title);
      alert.setContentText(content);
      alert.showAndWait();
  }

  public static void main(String[] args) {
      launch(args);
  }
}