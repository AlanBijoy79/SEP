import { useState } from "react";
import './App.css'
import inputDisplay from'./components/inputDisplay';
import ThemeSwitcher from "./components/ThemeSwitcher";

function App() 
{
  const[user,setUser] =useState("Aizal");
  return (
    <div className="App">
      <ThemeSwitcher />
    </div>
  );
}

export default App;