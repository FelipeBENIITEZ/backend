import { useEffect, useState } from "react";
import { getAllInscripciones } from "../api/Inscripciones.api";
import { Inscripcion_card } from "./Inscripcion_card";

export function Inscripciones_mostrar() {
  const [inscripcion, setInscripciones] = useState([]);

  useEffect(() => {
    async function loadInscripciones() {
      const ins = await getAllInscripciones();
      setInscripciones(ins.data);
    }
    loadInscripciones();
  }, []);

  return (
    <div className="grid grid-cols-3 gap-3">
      {inscripcion.map((inscripcion) => (
        <Inscripcion_card key={inscripcion.id} inscripcion={inscripcion} />
      ))}
    </div>
  );
}