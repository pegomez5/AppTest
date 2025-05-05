package com.example.test

import android.annotation.SuppressLint
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
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
    val userCreated by remember { mutableStateOf<User?>(null) }

    val users = remember { mutableStateListOf<User>() }

    Column(modifier.padding(16.dp)) {
        TextField(value = firstName, onValueChange = { firstName = it }, label = { Text("First Name") })
        TextField(value = lastName, onValueChange = { lastName = it }, label = { Text("Last Name") })
        TextField(value = email, onValueChange = { email = it }, label = { Text("Email") })
        TextField(value = username, onValueChange = { username = it }, label = { Text("Username") })
        TextField(value = password, onValueChange = { password = it }, label = { Text("Password") })
        Spacer(modifier = Modifier.height(16.dp))
        Button(onClick = {
            val newUser = User(
                firstName, lastName, email, username, password,
                isCoordinator = false,
                userID = Random.nextInt(0, 100),
                isActive = true,
                clubs = listOf("ClubA"),
                preferences = listOf("Pref1"),
            )
            users.add(newUser)
        }) {
            Text("Submit")
        }
        Spacer(modifier = Modifier.height(16.dp))
        userCreated?.let { it ->
            Text("Created user: ${it.firstName} ${it.lastName}" +
                    "\nEmail: ${it.email}" +
                    "\nUsername: ${it.username}" +
                    "\nUserID: ${it.userID}" +
                    "\nTotal users: ${users.size}" +
                    users.forEach {
                        Text("User: ${it.firstName} ${it.lastName}, Email: ${it.email}")
                    })

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




/*class Calendar (
    calendars: CharArray,
    events: CharArray,
    private val calenderId: Int,
    title: String,
    event: String,
    modifier: Modifier
): ComponentActivity() {
    @SuppressLint("UnusedMaterial3ScaffoldPaddingParameter")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent() {
            TestTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    CalanderTest(
                        userID = 0,
                        isActive = true,
                        //clubs = charArrayOf(),
                        //preferences = charArrayOf(),
                        firstName = "Hannah",
                        lastName = "Jeffers",
                        email = "hajeffers@ursinus.edu",
                        username = "hajeffers",
                        password = "password",
                        isCoordinator = false,
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }
}

    Calendar(this.title, [this.event]) {
        calendarId = Random().nextDouble();
    }

    void addCalendar(String calendar) {
        final hasCalendar = calendars.map((e) => e.toLowerCase()).toList();

        if (calendar.trim().isEmpty) {
            print("Calendar name cannot be empty.");
        } else if (hasCalendar.contains(calendar.toLowerCase())) {
            print("Calendar already exists.");
        } else {
            calendars.add(calendar.trim());
        }
    }

    void deleteCalendar(String target) {
        final trimmedTarget = target.trim();
        calendars.removeWhere((c) => c == trimmedTarget);
    }

    void addEvent(String event) {
        final hasEvent = events.map((e) => e.toLowerCase()).toList();

        if (hasEvent.contains(event.toLowerCase())) {
            print("Event is already on the calendar.");
        } else {
            events.add(event);
        }
    }

    static Calendar uploadCalendar(Map<String, dynamic> calendarData) {
        final title = calendarData['title'] ?? 'Untitled';
        final calendar = Calendar(title);

        final eventList = calendarData['events'] as List<dynamic>?;

        if (eventList != null) {
            for (var ev in eventList) {
                // Assuming events are simple strings for now
                calendar.addEvent(ev.toString());
            }
        }

        return calendar;
    }

    static Calendar? combineCalendars(Calendar c1, Calendar c2, String newTitle) {
        if (c1.calendarId == c2.calendarId) {
            return null;
        }

        final combined = Calendar(newTitle);
        combined.event = null; // Optional, depending on how events are structured

        // Append combined events to the global list (since that's your design)
        events.addAll([...eventsOf(c1), ...eventsOf(c2)]);

        return combined;
    }

    // Helper method for clarity
    static List<String> eventsOf(Calendar c) {
        // Here we assume global static events apply to all calendars (from your Python version)
        return events;
    }



@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    TestTheme {
        Greeting("Hannah")
    }
}*/

@Composable
fun UserTest(firstName: String, lastName: String, email: String, username: String, password: String, isCoordinator: Boolean, isActive: Boolean, userID: Int, modifier: Modifier) {
    Text(
        text = "First Name: $firstName\nLast Name: $lastName\nUsername: $username\nEmail: $email\nIs Active: $isActive\nIs Coordinator: $isCoordinator\n",
        modifier = modifier
    )

}

@Preview(showBackground = true)
@Composable
fun UserPreview() {
    TestTheme {
        UserTest(
            "Hannah", "Jeffers", "hajeffers@ursinus.edu", "hajeffers", "password", false, true, 0, Modifier
        )
    }
}

