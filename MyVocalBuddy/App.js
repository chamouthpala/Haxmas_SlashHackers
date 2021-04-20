import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import StartScreen from './src/views/start/Start';
import HomeScreen from './src/views/home/Home';
import AboutScreen from './src/views/about/about';
import SignInScreen from './src/views/sign-in/SignIn';
import VoiceRecScreen from './src/views/voiceRec/VoiceRec';
import SignUpScreen from './src/views/sign-up/SignUp';
import LoadingScreen from './src/views/loading/loading'
import TutorialScreen from './src/views/tutorial/tutorial';
import RecorderScreen from './src/views/recorder/Recorder';
import LoadingScreen from './src/views/Loading/loading';
import TutorialScreen from './src/views/tutorial/tutorial';
// import VoiceRecScreen from './src/views/voiceRec/voiceRec';
import 'react-native-gesture-handler';
// import { createStackNavigator, createAppContainer } from "react-navigation";
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from "@react-navigation/stack";
// import { createAppContainer } from "@react-navigation/native";
const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="SignIn">
        <Stack.Screen name="Start" component={StartScreen} />
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="About" component={AboutScreen} />
        <Stack.Screen name="SignIn" component={SignInScreen} />
        <Stack.Screen name="SignUp" component={SignUpScreen} />
        <Stack.Screen name="Loading" component={LoadingScreen} />
        <Stack.Screen name="Tutorials" component={TutorialScreen} />
        <Stack.Screen name="VoiceRec" component={VoiceRecScreen} />
        <Stack.Screen name="Loading" component={LoadingScreen} />
        <Stack.Screen name="Tutorial" component={TutorialScreen} />
        {/* <Stack.Screen name="Recorder" component={RecorderScreen} /> */}
      </Stack.Navigator>
    </NavigationContainer>
    
  );
}

const style = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
