import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Inscripciones_list } from "./paginas/Inscripciones_list";
import { Inscripciones_form } from "./paginas/Inscripciones_form";
import Navigation from "./components/Navigation";

function App() {
  return (
    <Router>
      <Navigation />
      <Routes>
        <Route path="/" element={<Inscripciones_list />} />
        <Route path="/Inscripciones" element={<Inscripciones_list />} />
        <Route path="/Inscripcion-create" element={<Inscripciones_form />} />
        <Route path="/Inscripcion-edit/:id" element={<Inscripciones_form />} />
      </Routes>
    </Router>
  );
}

export default App;
