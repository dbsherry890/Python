import React, { useState } from "react";

const AddGiftForm = ({ addGift }) => {
  const [giftName, setGiftName] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    if (giftName) {
      addGift(giftName);
      setGiftName("");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={giftName}
        onChange={(e) => setGiftName(e.target.value)}
        placeholder="Enter gift name"
      />
      <button type="submit">Add Gift</button>
    </form>
  );
};

export default AddGiftForm;
