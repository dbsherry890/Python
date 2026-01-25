import React, { useEffect, useState } from "react";
import api from "../api.js";
import AddGiftForm from "./AddGiftForm.jsx";

const GiftList = () => {
  const [gifts, setGifts] = useState([]);

  const fetchGifts = async () => {
    try {
      const response = await api.get("/gifts");
      setGifts(response.data.gifts);
    } catch (error) {
      console.error("Error fetching gifts", error);
    }
  };

  const addGift = async (giftName) => {
    try {
      await api.post("/gifts", { name: giftName });
      fetchGifts(); // Refresh the list after adding a gift
    } catch (error) {
      console.error("Error adding gift", error);
    }
  };

  useEffect(() => {
    fetchGifts();
  }, []);

  return (
    <div>
      <h2>Gifts List</h2>
      <ul>
        {gifts.map((gift, index) => (
          <li key={index}>{gift.name}</li>
        ))}
      </ul>
      <AddGiftForm addGift={addGift} />
    </div>
  );
};

export default GiftList;
