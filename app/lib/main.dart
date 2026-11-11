//import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:tflite_flutter/tflite_flutter.dart';
import 'dart:io';
import 'dart:typed_data';
import 'package:flutter/services.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Plant Disease Detection',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.green),
        useMaterial3: true,
      ),
      home: const PlantDiseasePage(),
    );
  }
}

class PlantDiseasePage extends StatefulWidget {
  const PlantDiseasePage({super.key});

  @override
  State<PlantDiseasePage> createState() => _PlantDiseasePageState();
}

class _PlantDiseasePageState extends State<PlantDiseasePage> {
  File? _image;
  String _result = "පින්තූරයක් තෝරන්න";
  bool _isLoading = false;

  // අපේ TFLite Model එක පාවිච්චි කරන්න
  Interpreter? _interpreter;

  @override
  void initState() {
    super.initState();
    _loadModel();
  }

  // Model එක load කරන function එක
  Future<void> _loadModel() async {
    print('✅ Model load කරන්න සූදානම්!');
  }

  // පින්තූරයක් තෝරන function එක
  Future<void> _pickImage() async {
    final picker = ImagePicker();
    final pickedFile = await picker.pickImage(source: ImageSource.gallery);

    if (pickedFile != null) {
      setState(() {
        _image = File(pickedFile.path);
        _result = "පරීක්ෂා කරමින්...";
        _isLoading = true;
      });
      // මෙතනදී අපි පස්සේ TFLite Model එකට පින්තූරය දෙන්න ඕනේ
      // දැනට අපි පොඩි test එකක් කරමු
      await Future.delayed(const Duration(seconds: 2));
      setState(() {
        _result = "මෙය පරීක්ෂණාත්මක ප්‍රතිඵලයකි. (Model එක ඉක්මනින් connect වේ)";
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Plant Disease Detection'),
        backgroundColor: Colors.green,
        foregroundColor: Colors.white,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // පින්තූරය පෙන්නන තැන
            Container(
              width: 300,
              height: 300,
              decoration: BoxDecoration(
                border: Border.all(color: Colors.grey),
                borderRadius: BorderRadius.circular(12),
              ),
              child: _image != null
                  ? ClipRRect(
                      borderRadius: BorderRadius.circular(12),
                      child: Image.file(_image!, fit: BoxFit.cover),
                    )
                  : const Center(child: Text("පින්තූරයක් නැත")),
            ),
            const SizedBox(height: 20),
            
            // ප්‍රතිඵලය පෙන්නන තැන
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Text(
                _result,
                style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                textAlign: TextAlign.center,
              ),
            ),
            const SizedBox(height: 20),
            
            // පින්තූරය තෝරන්න බොත්තම
            ElevatedButton.icon(
              onPressed: _isLoading ? null : _pickImage,
              icon: const Icon(Icons.photo_library),
              label: const Text('පින්තූරයක් තෝරන්න'),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.green,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15),
              ),
            ),
            if (_isLoading)
              const Padding(
                padding: EdgeInsets.all(20.0),
                child: CircularProgressIndicator(),
              ),
          ],
        ),
      ),
    );
  }
}