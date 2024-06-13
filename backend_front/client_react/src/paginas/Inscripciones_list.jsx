// src/pages/Inscripciones_list.jsx

import React, { useEffect, useState } from "react";
import { getAllInscripciones } from "../api/Inscripciones.api";
import Inscripciones_mostrar from "../components/Inscripciones_mostrar";

export function Inscripciones_list() {
  const [inscripciones, setInscripciones] = useState([]);

  useEffect(() => {
    async function fetchInscripciones() {
      const response = await getAllInscripciones();
      setInscripciones(response.data);
    }

    fetchInscripciones();
  }, []);

  return (
    <div>
      <Inscripciones_mostrar inscripciones={inscripciones} />
    </div>
  );
}
