# DevOps Learning

Portafolio de proyectos progresivos para practicar cómo desplegar, automatizar y operar aplicaciones. Cada proyecto documenta su objetivo, arquitectura, instrucciones reproducibles, decisiones técnicas y problemas encontrados.

## Ruta de proyectos

| Proyecto | Objetivo | Tecnologías principales | Estado |
|---|---|---|---|
| [01 — Docker + CI/CD](./projects/01-docker-cicd/README.md) | Aplicación de tres capas, contenedores, pipeline, análisis de imágenes y primer despliegue | Python, Flask, PostgreSQL, HTML/CSS/JavaScript | Aplicación local; CI y contenedores en progreso |
| [02 — Cloud deployment](./projects/02-cloud-deployment/README.md) | Desplegar la aplicación en una plataforma cloud y documentar el resultado | Cloud, infraestructura como código por definir | Pendiente |
| [03 — Kubernetes](./projects/03-kubernetes/README.md) | Ejecutar la aplicación en K3s o Minikube | Kubernetes, Helm | Pendiente |
| [04 — Terraform](./projects/04-terraform/README.md) | Profundizar en la gestión reproducible de infraestructura | Terraform, proveedor cloud por definir | Pendiente |
| [05 — GitOps](./projects/05-gitops/README.md) | Sincronizar cambios declarativos con Kubernetes | Argo CD | Pendiente |
| [06 — Production platform](./projects/06-production-platform/README.md) | Incorporar observabilidad, alertas y prácticas de seguridad | Prometheus, Grafana, stack de logs | Pendiente |

> Los proyectos reutilizarán la aplicación del Proyecto 1 cuando sea útil. El foco está en la infraestructura y en la operación, no en crear una aplicación distinta para cada herramienta.

## Proyecto inicial

El Proyecto 1 contiene una aplicación sencilla con frontend, API REST y PostgreSQL. Incluye instrucciones para ejecutarla localmente, datos de ejemplo y pruebas automatizadas. El reto DevOps avanza por iteraciones: Compose, CI y construcción/escaneo de imágenes están en desarrollo; el despliegue y la publicación de imágenes todavía deben demostrarse.

## Evidencias y documentación

- [Documentación general](./docs/README.md)
- [Guía de troubleshooting](./docs/troubleshooting.md)
- Cada proyecto mantiene sus instrucciones, diagrama, decisiones, problemas y evidencias en su propio directorio.

## Trabajá por entregables, no por semanas

Medí el progreso por resultados verificables, no por el tiempo que llevás estudiando una herramienta. No avances al siguiente gran objetivo solo porque terminó la semana: hacelo cuando la solución actual funcione y puedas explicar por qué.

### Proyecto 1: Checklist de entregables

- [x] La aplicación funciona localmente: frontend, API y PostgreSQL se comunican.
- [x] Docker Compose funciona: servicios, redes, persistencia y healthchecks.
- [x] Seguridad integrada: Trivy analiza las imágenes y está definido cómo tratar vulnerabilidades.
- [x] Imágenes publicadas en un registry con tags reproducibles y versiones.
- [ ] Aplicación desplegada en una VM, con configuración segura y HTTPS.
- [ ] Documentación terminada: diagrama, instrucciones, troubleshooting y evidencias.

El checklist detallado y los problemas encontrados se mantienen en el [README del Proyecto 1](./projects/01-docker-cicd/README.md#checklist-de-entregables). Primero poné la aplicación en línea; después automatizá y mejorá la solución en iteraciones. No hace falta tener Docker, Kubernetes, Terraform, GitOps y observabilidad perfectos antes del primer despliegue.

## Las cinco preguntas para cada proyecto

Documentá y respondé estas preguntas en cada proyecto:

1. ¿Qué problema estoy resolviendo?
2. ¿Cómo diseñé la solución y por qué?
3. ¿Cómo la desplegué desde cero?
4. ¿Qué falló y cómo lo diagnostiqué?
5. ¿Cómo demostraría que funciona y que es segura?

Estas respuestas conectan las decisiones técnicas con la operación real y te ayudan a explicar tu experiencia en entrevistas. Avanzá cuando puedas desplegar el proyecto desde cero, demostrar que funciona y explicar sus decisiones y diagnóstico.

## Crear un nuevo proyecto con ayuda de IA

Al iniciar un proyecto, podés usar este prompt y adaptar el nombre y los requisitos de la aplicación. La IA debe entregar la aplicación que vas a desplegar, no resolver el reto DevOps:

> Quiero practicar DevOps mediante proyectos progresivos y realistas.
>
> Actuá como un ingeniero de software que me entrega aplicaciones para desplegar, no como alguien que hace mi trabajo de DevOps.
>
> Para el proyecto **[nombre o número del proyecto]**, generá una aplicación sencilla de tres capas:
>
> - Frontend web.
> - Backend con API REST.
> - PostgreSQL.
>
> Requisitos:
>
> 1. La aplicación debe funcionar localmente y permitir verificar que frontend, API y base de datos se comunican correctamente.
> 2. Incluí pruebas automatizadas y documentación de los endpoints.
> 3. Proporcioná el código fuente, un README funcional y datos de prueba.
> 4. No generes Dockerfiles, Docker Compose, pipelines CI/CD, Terraform, manifiestos Kubernetes ni configuración de GitOps.
> 5. No compliques innecesariamente el código de aplicación.
>
> Entregá primero los requisitos, la arquitectura, los criterios de aceptación y el código fuente.
>
> Mi responsabilidad será diseñar, implementar, probar y documentar toda la solución DevOps. No me des la solución completa por adelantado. Ayudame a investigar los problemas cuando te muestre lo que intenté.

## Flujo de colaboración

Trabajá en una rama por cambio y abrí un pull request (PR) hacia `main` para revisar e integrar el trabajo. Por ejemplo:

```bash
git switch -c feature/docker
```

Usá [Conventional Commits](https://www.conventionalcommits.org/) para que el propósito de cada cambio quede claro:

```text
<tipo>(<alcance>): <descripción breve>
```

Tipos habituales:

- `feat`: nueva funcionalidad.
- `fix`: corrección de un error.
- `docs`: documentación.
- `test`: pruebas.
- `ci`: integración continua.
- `build`: dependencias o sistema de compilación.
- `refactor`: cambio interno sin alterar comportamiento.

Ejemplos:

```text
docs(project-01): documentar arquitectura y criterios de aceptación
feat(api): agregar endpoint de salud de PostgreSQL
ci(project-01): ejecutar pruebas en pull requests
```

Antes de solicitar revisión, comprobá que las pruebas relevantes pasan, que la documentación refleja el cambio y que no se incluyeron secretos. En la descripción del PR, explicá el objetivo, las decisiones, cómo probarlo y cualquier problema conocido; vinculá evidencias cuando existan. Tras la revisión y las comprobaciones, integrá el PR en `main`.
