# Ruta de Aprendizaje para AWS

## 1. Fundamentos (Semanas 1-2)
### Servicios esenciales:
- Redes: VPC, Subnets, Security Groups, Route Tables.
- Almacenamiento: S3, EBS, EFS.
- Cómputo: EC2, AWS Lambda, ECS.
- Bases de datos: RDS, DynamoDB.

### Recursos sugeridos:
- [AWS Cloud Practitioner Essentials (Curso oficial)](https://aws.amazon.com/training/)
- [Documentación oficial de AWS](https://aws.amazon.com/documentation/)
- Laboratorios prácticos básicos con la cuenta gratuita:
  - Crear un bucket de S3.
  - Desplegar una instancia EC2.

---

## 2. Redes y Arquitectura (Semanas 3-4)
### Tareas clave:
- Crear una VPC personalizada con subnets públicas y privadas.
- Configurar NAT Gateway e Internet Gateway.
- Implementar un balanceador de cargas (ALB).

### Recursos sugeridos:
- [Curso de Udemy: AWS Certified Solutions Architect Associate](https://www.udemy.com/)
- Laboratorios de AWS Hands-On:
  - Configuración de VPC y ALB.
  - Despliegue básico de aplicaciones web.

---

## 3. Automatización y Herramientas Avanzadas (Semanas 5-6)
### Tareas clave:
- Infraestructura como código (IaC):
  - Uso de AWS CloudFormation o Terraform.
- Configuración de CI/CD:
  - AWS CodePipeline, CodeBuild, y CodeDeploy.
- Uso de API Gateway y Lambda para microservicios.

### Recursos sugeridos:
- [Curso introductorio a Terraform](https://www.udemy.com/)
- Documentación oficial de AWS API Gateway y Lambda.
- Ejercicios prácticos:
  - Desplegar un servicio con API Gateway y Lambda.
  - Implementar un stack automatizado con CloudFormation.

---

## 4. Proyecto Completo (Semana 7+)
### Objetivo:
Implementar un stack completo en AWS con:
- DNS (Route 53).
- Balanceadores de cargas (ALB y NLB).
- Certificado SSL aplicado.
- Redirección de tráfico hacia funciones Lambda y contenedores en ECS.

### Pasos:
1. Diseñar un diagrama de arquitectura.
2. Implementar cada componente de forma separada:
   - Configurar Route 53 con DNS y certificado SSL.
   - Configurar ALB y NLB.
   - Desplegar contenedores en ECS.
3. Integrar todos los componentes en un stack funcional.
4. Monitorear y asegurar la infraestructura con CloudWatch e IAM.

---

## 5. Preparación para Certificación (Opcional)
### Certificaciones sugeridas:
- **Nivel asociado:** AWS Certified Solutions Architect – Associate.
- **Nivel avanzado:** AWS Certified Solutions Architect – Professional.

### Recursos:
- [AWS Skill Builder](https://skillbuilder.aws/)
- [Mock Exams y preguntas prácticas](https://www.whizlabs.com/)

---

## Recursos adicionales
- [Documentación oficial de AWS](https://aws.amazon.com/documentation/)
- [AWS Free Tier](https://aws.amazon.com/free/)
- Comunidades:
  - Reddit: [r/aws](https://www.reddit.com/r/aws/)
  - Discord: Servidores especializados en AWS.

