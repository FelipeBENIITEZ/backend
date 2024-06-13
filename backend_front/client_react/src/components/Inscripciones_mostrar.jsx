import React from "react";
import { Inscripcion_card } from "./Inscripcion_card";

function Inscripciones_mostrar({ inscripciones }) {
  console.log("Props received in Inscripciones_mostrar:", inscripciones); // Verifica las props aquí
  return (
    <div className="grid grid-cols-3 gap-3">
      {inscripciones.map((inscripcion) => (
        <Inscripcion_card key={inscripcion.id} inscripcion={inscripcion} />
      ))}
    </div>
  );
}

export default Inscripciones_mostrar;
