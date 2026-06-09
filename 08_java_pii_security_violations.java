/**
 * Java Test File for Guardrails Testing
 * Contains PII violations, security issues, and hardcoded credentials
 * Expected Violations: 15-20 PII/Security violations
 * Severity Range: High to Critical (3-4)
 */

package com.example.security;

import java.sql.*;
import java.util.*;

public class UserManagementSystem {
    
    // VIOLATION: Hardcoded credentials
    private static final String DB_PASSWORD = "Admin@123456";
    private static final String API_KEY = "sk-proj-abc123xyz789-REAL-API-KEY-HERE";
    private static final String AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";
    
    // VIOLATION: PII in comments and code
    // John Smith's SSN: 123-45-6789
    // Credit Card: 4532-1234-5678-9010
    // Email: john.smith@company.com
    // Phone: +1-555-123-4567
    
    public class User {
        private String ssn = "987-65-4321"; // VIOLATION: SSN in code
        private String creditCard = "5425233430109903"; // VIOLATION: Credit card
        private String email = "admin@internal-company.com"; // VIOLATION: Email
        private String phoneNumber = "+1-202-555-0147"; // VIOLATION: Phone
        private String address = "123 Main Street, New York, NY 10001"; // VIOLATION: Address
        private String passportNumber = "P12345678"; // VIOLATION: Passport
        private String driverLicense = "DL-NY-12345678"; // VIOLATION: Driver's license
        private String bankAccount = "1234567890123456"; // VIOLATION: Bank account
        private String medicalRecordId = "MRN-987654321"; // VIOLATION: Medical record
        private String ipAddress = "192.168.1.100"; // VIOLATION: IP address
    }
    
    // VIOLATION: SQL Injection vulnerability
    public User getUserByUsername(String username) throws SQLException {
        Connection conn = DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/userdb",
            "root",
            DB_PASSWORD // VIOLATION: Using hardcoded password
        );
        
        // VIOLATION: SQL Injection - no prepared statement
        String query = "SELECT * FROM users WHERE username = '" + username + "'";
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);
        
        return null;
    }
    
    // VIOLATION: Logging sensitive data
    public void logUserActivity(String ssn, String creditCard) {
        System.out.println("User SSN: " + ssn); // VIOLATION: Logging PII
        System.out.println("Credit Card: " + creditCard); // VIOLATION: Logging PII
        System.out.println("API Key: " + API_KEY); // VIOLATION: Logging credentials
    }
    
    // VIOLATION: Insecure password storage
    public void createUser(String username, String password) {
        // VIOLATION: Storing password in plain text
        String insertQuery = "INSERT INTO users (username, password) VALUES ('" 
            + username + "', '" + password + "')";
        // No password hashing!
    }
    
    // VIOLATION: Weak encryption
    public String encryptData(String data) {
        // VIOLATION: Using deprecated/weak encryption
        return Base64.getEncoder().encodeToString(data.getBytes());
        // Base64 is encoding, not encryption!
    }
    
    // VIOLATION: Exposing internal system information
    public Map<String, String> getSystemInfo() {
        Map<String, String> info = new HashMap<>();
        info.put("database_host", "prod-db-01.internal.company.com"); // VIOLATION
        info.put("admin_email", "sysadmin@company.com"); // VIOLATION
        info.put("backup_server", "10.0.0.50"); // VIOLATION: Internal IP
        info.put("encryption_key", "MySecretKey123"); // VIOLATION: Hardcoded key
        return info;
    }
    
    // VIOLATION: Insecure random number generation
    public String generateToken() {
        Random random = new Random(); // VIOLATION: Not cryptographically secure
        return String.valueOf(random.nextInt());
    }
    
    // VIOLATION: Path traversal vulnerability
    public String readFile(String filename) throws Exception {
        // VIOLATION: No path validation
        return new String(java.nio.file.Files.readAllBytes(
            java.nio.file.Paths.get("/var/data/" + filename)
        ));
    }
    
    // VIOLATION: XXE (XML External Entity) vulnerability
    public void parseXML(String xmlContent) throws Exception {
        javax.xml.parsers.DocumentBuilderFactory factory = 
            javax.xml.parsers.DocumentBuilderFactory.newInstance();
        // VIOLATION: XXE not disabled
        javax.xml.parsers.DocumentBuilder builder = factory.newDocumentBuilder();
        builder.parse(new java.io.ByteArrayInputStream(xmlContent.getBytes()));
    }
    
    // VIOLATION: Insecure deserialization
    public Object deserializeObject(byte[] data) throws Exception {
        // VIOLATION: Deserializing untrusted data
        java.io.ObjectInputStream ois = new java.io.ObjectInputStream(
            new java.io.ByteArrayInputStream(data)
        );
        return ois.readObject();
    }
    
    // VIOLATION: Command injection vulnerability
    public void executeCommand(String userInput) throws Exception {
        // VIOLATION: Executing user input without validation
        Runtime.getRuntime().exec("ping " + userInput);
    }
    
    // Test data with PII violations
    private static final String[] TEST_USERS = {
        "SSN: 111-22-3333, Name: Alice Johnson",
        "SSN: 444-55-6666, Name: Bob Williams",
        "Email: charlie.brown@example.com, Phone: 555-987-6543",
        "Credit Card: 4111111111111111, CVV: 123",
        "Passport: A98765432, DOB: 01/15/1985"
    };
}

// Made with Bob
