import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import Room from "./Room";
import {
  BrowserRouter,
  Routes,
  Route,
  // Link,
  // Redirect,
} from "react-router-dom";

export default function Homepage() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/join" element={<RoomJoinPage />} />
        <Route path="/create" element={<CreateRoomPage />} />
        <Route path="/room/:roomCode" element={<Room />} />
        <Route exact path="/" element={<p>This is the home page</p>} />
      </Routes>
    </BrowserRouter>
  );
}
