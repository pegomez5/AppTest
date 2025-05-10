import 'dart:math';

class User {
  String firstName;
  String lastName;
  String email;
  String username;
  String password;
  bool isCoordinator;
  final int userId;
  bool isActive;
  List<String> clubs = [];
  List<String> preferences = [];

  User({
    required this.firstName,
    required this.lastName,
    required this.email,
    required this.username,
    required this.password,
    required this.isCoordinator,
    bool? isActive,
    int? userId,
  })  : this.isActive = isActive ?? true,
        this.userId = userId ?? Random().nextInt(100);
}
