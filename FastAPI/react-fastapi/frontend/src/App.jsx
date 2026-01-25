// import React from "react";
import "./App.css";
import GiftList from "./components/Gifts";

const App = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Gift Management App</h1>
      </header>
      <main>
        <GiftList />
      </main>
    </div>
  );
};

export default App;
