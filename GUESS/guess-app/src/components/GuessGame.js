import React, {useState}  from "react";
import "./GuessGame.css";
function GuessGame() {
    const [targetNumeber , setTargetNumber] = useState(
        Math.floor(Math.random() * 100) + 1
    );
    const [guess,setGuess] = useState("");
    const [attempts, setFeedback]}