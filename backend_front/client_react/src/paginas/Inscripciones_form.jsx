import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";
import { createInscripcion, updateInscripcion, getInscripcion, getTutorAlumnos } from "../api/Inscripciones.api";
import { toast } from "react-hot-toast";
export function Inscripciones_form() {
    const {
        register,
        handleSubmit,
        formState: { errors },
        setValue,
        watch
    } = useForm();
    const navigate = useNavigate();
    const params = useParams();
    const [tutorAlumnos, setTutorAlumnos] = useState([]);

    const niveles = ["Escolar Básica", "Educación Media", "Nivel Inicial"];
    const gradosInicial = ["Pre-Jardín", "Jardín", "Preescolar"];
    const gradosEscolar = ["1º", "2º", "3º", "4º", "5º", "6º", "7º", "8º", "9º"];
    const gradosMedia = ["1º", "2º", "3º"];
    const ciclosEscolar = ["1º", "2º", "3º"];
    const ciclosMedia = ["Bachillerato"];
    const turnosEscolar = ["Mañana", "Tarde"];
    const turnosInicial = [""];
    const turnosMedia = [""];
    const especializacionesMedia = ["Ciencias Básicas", "Ciencias Sociales", "BTI", "BTA"];

    const nivel = watch("nivel");

    const onSubmit = handleSubmit(async (data) => {
        console.log("Submitting data:", data);  // Log the form data

        try {
            // Separar los datos para Inscripciones y Aranceles
            const inscripcionData = {
                tutor_alumno: data.tutor_alumno,
                ins_contrato_fecha: data.ins_contrato_fecha,
                ins_estado: data.ins_estado,
                ins_periodo: data.ins_periodo,
                nivel: data.nivel,
                ins_habilitacion: true,  // Suponiendo que es true por defecto o se determina lógicamente
            };

            const arancelData = {
                arancel_nivel: data.nivel,
                arancel_ciclo: data.ciclo,
                arancel_especializacion: data.especializacion,
                arancel_grado: data.grado,
                arancel_turno: data.turno,
            };

            if (params.id) {
                await updateInscripcion(params.id, inscripcionData);
                // Si necesitas enviar a aranceles también, realiza la llamada correspondiente
                toast.success("Inscripción Actualizada", {
                    position: "bottom-right",
                    style: {
                        background: "#101010",
                        color: "#fff",
                    },
                });
            } else {
                await createInscripcion(inscripcionData);
                // Si necesitas enviar a aranceles también, realiza la llamada correspondiente
                toast.success("Nueva Inscripción agregada", {
                    position: "bottom-right",
                    style: {
                        background: "#101010",
                        color: "#fff",
                    },
                });
            }
            navigate("/Inscripciones");
        } catch (error) {
            console.error("Error saving inscripcion:", error);  // Log the error
            toast.error("Error guardando la inscripción. Por favor, revisa los datos e intenta de nuevo.", {
                position: "bottom-right",
                style: {
                    background: "#101010",
                    color: "#fff",
                },
            });
        }
    });

    useEffect(() => {
        async function loadInscripcion() {
            if (params.id) {
                const { data } = await getInscripcion(params.id);
                setValue("tutor_alumno", data.tutor_alumno);
                setValue("ins_contrato_fecha", data.ins_contrato_fecha);
                setValue("ins_estado", data.ins_estado);
                setValue("ins_periodo", data.ins_periodo);
                setValue("nivel", data.nivel);
                setValue("ciclo", data.ciclo);
                setValue("curso", data.curso);
                setValue("turno", data.turno);
                setValue("especializacion", data.especializacion);
            }
        }
        loadInscripcion();

        async function loadTutorAlumnos() {
            const { data } = await getTutorAlumnos();
            setTutorAlumnos(data);
        }
        loadTutorAlumnos();
    }, [params.id, setValue]);

    return (
        <div className="max-w-xl mx-auto">
            <form onSubmit={onSubmit} className="bg-zinc-800 p-10 rounded-lg mt-2">
                <select
                    {...register("tutor_alumno", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                >
                    <option value="">Seleccionar Tutor/Alumno</option>
                    {tutorAlumnos.map((tutorAlumno) => (
                        <option key={tutorAlumno.id} value={tutorAlumno.id}>
                            {tutorAlumno.tutor.tut_nom} {tutorAlumno.tutor.tut_ape} - {tutorAlumno.alumno.alu_nom} {tutorAlumno.alumno.alu_ape}
                        </option>
                    ))}
                </select>
                {errors.tutor_alumno && <span>Este campo es requerido</span>}

                <input
                    type="date"
                    placeholder="Fecha de Contrato"
                    {...register("ins_contrato_fecha", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.ins_contrato_fecha && <span>Este campo es requerido</span>}
                    
                <select
                    {...register("ins_estado", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                >
                    <option value="">Seleccionar Estado</option>
                    <option value="Pagado">Pagado</option>
                    <option value="Pendiente">Pendiente</option>
                    <option value="Inscripto">Inscripto</option>
                </select>
                {errors.ins_estado && <span>Este campo es requerido</span>}

                <input
                    type="text"
                    placeholder="Período"
                    {...register("ins_periodo", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                />
                {errors.ins_periodo && <span>Este campo es requerido</span>}

                <select
                    {...register("nivel", { required: true })}
                    className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                >
                    <option value="">Seleccione el nivel</option>
                    {niveles.map((nivel) => (
                        <option key={nivel} value={nivel}>
                            {nivel}
                        </option>
                    ))}
                </select>
                {errors.nivel && <span>Este campo es requerido</span>}

                {/* Mostrar campos adicionales según el nivel seleccionado */}
                {nivel === "Escolar Básica" && (
                    <>
                        <select
                            {...register("ciclo", { required: true })}
                            className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                        >
                            <option value="">Seleccione el ciclo</option>
                            {ciclosEscolar.map((ciclo) => (
                                <option key={ciclo} value={ciclo}>
                                    {ciclo}
                                </option>
                            ))}
                        </select>
                        {errors.ciclo && <span>Este campo es requerido</span>}

                        <select
                            {...register("grado", { required: true })}
                            className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                        >
                            <option value="">Seleccione el grado</option>
                            {gradosEscolar.map((grado) => (
                                <option key={grado} value={grado}>
                                    {grado}
                                </option>
                            ))}
                        </select>
                        {errors.grado && <span>Este campo es requerido</span>}

                        <select
                            {...register("turno", { required: true })}
                            className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                        >
                            <option value="">Seleccione el turno</option>
                            {turnosEscolar.map((turno) => (
                                <option key={turno} value={turno}>
                                    {turno}
                                </option>
                            ))}
                        </select>
                        {errors.turno && <span>Este campo es requerido</span>}
                    </>
                )}

                {nivel === "Educación Media" && (
                    <>
                        <select
                            {...register("ciclo", { required: true })}
                            className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                        >
                            <option value="">Seleccione el ciclo</option>
                            {ciclosMedia.map((ciclo) => (
                                <option key={ciclo} value={ciclo}>
                                    {ciclo}
                                </option>
                            ))}
                        </select>
                        {errors.ciclo && <span>Este campo es requerido</span>}

                        <select
                            {...register("especializacion", { required: true })}
                            className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
                        >
                            <option value="">Seleccione la especialización</option>
                            {especializacionesMedia.map((especializacion) => (
                                <option key={especializacion} value={especializacion}>
                                    {especializacion}
                                </option>
                            ))}
                        </select>
                        {errors.especializacion && <span>Este campo es requerido</span>}
                    </>
                )}

                {/* Botón de envío */}
                <button
                    type="submit"
                    className="bg-blue-500 text-white p-3 rounded-lg w-full mt-4"
                >
                    {params.id ? "Actualizar Inscripción" : "Agregar Inscripción"}
                </button>
            </form>
        </div>
    );
}

export default Inscripciones_form;
