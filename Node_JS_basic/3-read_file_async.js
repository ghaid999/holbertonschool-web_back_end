const fs = require("fs");

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, "utf8", (error, data) => {
      if (error) {
        reject(new Error("Cannot load the database"));
        return;
      }

      const lines = data.split("\n");

      const students = lines
        .slice(1)
        .filter((line) => line.trim() !== "");

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

      resolve();
    });
  });
}

module.exports = countStudents;
