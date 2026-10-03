const fs = require("fs");

function countStudents(path) {
  let data;

  try {
    data = fs.readFileSync(path, "utf8");
  } catch (error) {
    throw new Error("Cannot load the database");
  }

  const lines = data.split("\n");
  const students = lines.slice(1).filter((line) => line.trim() !== "");

  console.log(`Number of students: ${students.length}`);

  const studentsByField = {};

  students.forEach((student) => {
    const [firstname, lastname, age, field] = student.split(",");

    if (!studentsByField[field]) {
      studentsByField[field] = [];
    }

    studentsByField[field].push(firstname);
  });

  Object.keys(studentsByField).forEach((field) => {
    const names = studentsByField[field];

    console.log(
      `Number of students in ${field}: ${names.length}. List: ${names.join(", ")}`
    );
  });
}

module.exports = countStudents;
