import React from "react";

function InfoPage() {
  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle form submission
    alert("Formulaire envoyé!");
  };

  return (
    <div>
      <h1>Entrez vos informations</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Nom de l'entreprise: <input type="text" name="Nom de l'entreprise" required />
        </label>
        <br />
        <label>
          email: <input type="email" name="email" required />
        </label>
        <br />
        <button type="submit">Envoyer</button>
      </form>
    </div>
  );
}

export default InfoPage;