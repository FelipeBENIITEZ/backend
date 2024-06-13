import { Link } from "react-router-dom";

export default function Navigation() {
  return (
    <div className="flex justify-between py-3 items-center">
      <Link to="/Inscripciones">
        <h1 className="font-bold text-3xl mb-4">INSCRIPCIONES</h1>
      </Link>
      <button className="bg-indigo-500 p-3 rounded-lg">
        <Link to="/Inscripcion-create">INSCRIBIR ALUMNO</Link>
      </button>
    </div>
  );
}