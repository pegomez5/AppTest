package com.example.test

import android.annotation.SuppressLint
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Checkbox
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.test.ui.theme.TestTheme
import kotlin.random.Random
import java.util.Scanner

/*class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            TestTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    Greeting(
                        name = "Hannah",
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }
}*/

// Data class to store user input
data class User(
    val firstName: String,
    val lastName: String,
    val email: String,
    val username: String,
    val password: String,
    val isCoordinator: Boolean,
    val userID: Int,
    val isActive: Boolean,
    val clubs: List<String>,
    val preferences: List<String>
)

// Composable Form
@Composable
fun UserForm(modifier: Modifier = Modifier) {
    var firstName by remember { mutableStateOf("") }
    var lastName by remember { mutableStateOf("") }
    var email by remember { mutableStateOf("") }
    var username by remember { mutableStateOf("") }
    var password by remember { mutableStateOf("") }
    var isCoordinator by remember { mutableStateOf(false) }

    var newUser by remember { mutableStateOf<User?>(null) }

    val users = remember { mutableStateListOf<User>() }

    Column(modifier.padding(16.dp)) {
        TextField(value = firstName, onValueChange = { firstName = it }, label = { Text("First Name") })
        TextField(value = lastName, onValueChange = { lastName = it }, label = { Text("Last Name") })
        TextField(value = email, onValueChange = { email = it }, label = { Text("Email") })
        TextField(value = username, onValueChange = { username = it }, label = { Text("Username") })
        TextField(value = password, onValueChange = { password = it }, label = { Text("Password") })
        Spacer(modifier = Modifier.height(16.dp))

        Row(
            verticalAlignment = Alignment.CenterVertically,
            modifier = Modifier.padding(top = 8.dp)
        ) {
            Checkbox(
                checked = isCoordinator,
                onCheckedChange = { isCoordinator = it }
            )
            Text("Are you a coordinator?")
        }

        Spacer(modifier = Modifier.height(16.dp))

        val isFormValid = firstName.isNotBlank() &&
                lastName.isNotBlank() &&
                email.contains("@") &&
                email.isNotBlank() &&
                (email.contains(".edu") ||
                        email.contains(".org") ||
                        email.contains(".com") ||
                        email.contains(".net")) &&
                username.isNotBlank() &&
                password.isNotBlank()
        Button (
            onClick = {
                newUser = User(
                    firstName, lastName, email, username, password,
                    isCoordinator = isCoordinator,
                    userID = Random.nextInt(0, 1000000),
                    isActive = true,
                    clubs = listOf("ClubA"),
                    preferences = listOf("Pref1"),
                )
                users.add(newUser!!)
            },
            enabled = isFormValid
        )

        {
            Text("Submit")
        }
        if (!isFormValid) {
            Text("Please fill out all required fields and use a valid email/password", color = Color.Red, fontSize = 12.sp)
        }
        Spacer(modifier = Modifier.height(16.dp))
        newUser?.let { it ->
            Text("Created user: ${it.firstName} ${it.lastName}" +
                    "\nEmail: ${it.email}" +
                    "\nUsername: ${it.username}" +
                    "\nUserID: ${it.userID}" +
                    "\nIsCoordinator: ${it.isCoordinator}")

        }
    }
}

// MainActivity setup
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            TestTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    UserForm(modifier = Modifier.padding(innerPadding))
                }
            }
        }
    }
}


