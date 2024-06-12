import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Navigation } from "./components/Navigation";
import { Inscripciones_form } from "./paginas/Inscripciones_form";
import { Inscripciones_list } from "./paginas/Inscripciones_list";
import { Toaster } from "react-hot-toast";
import axios from 'axios';
axios.defaults.withCredentials = true;
function App() {
  return (
    <BrowserRouter>
      <div className="container mx-auto">
        <Navigation />
        <Routes>
          {/* redirect to tasks */}
          <Route path="/" element={<Navigate to="/Inscripciones" />} />
          <Route path="/Inscripciones" element={<Inscripciones_list />} />
          <Route path="/Inscripciones/:id" element={<Inscripciones_form />} />
          <Route path="/Inscripciones-create" element={<Inscripciones_form />} />
        </Routes>
        <Toaster />
      </div>
    </BrowserRouter>
  );
}

export default App;