# Grazioso Salvare Dashboard Project - GitHub Repository README
# Jannatul Ferdush

Welcome to the repository for my **Grazioso Salvare Dashboard Project**! This project demonstrates a full-stack dashboard designed to support Grazioso Salvare's mission to identify suitable dogs for search-and-rescue training, helping the organization better identify dogs based on specific characteristics and rescue needs. Below, I address key questions related to this project, reflecting on the process and broader goals of computer science in solving practical challenges.

---

## How do you write programs that are maintainable, readable, and adaptable?

Writing maintainable, readable, and adaptable code requires consistency, modular design, and clear documentation. In this project, I developed a **CRUD Python module** to streamline database interactions with MongoDB, making the codebase cleaner and easier to manage. This modular approach allowed me to separate database logic from the dashboard’s user interface, simplifying the structure and enabling efficient debugging. This approach has long-term benefits: if Grazioso Salvare or any other client needed to adapt the dashboard in the future, the CRUD module could easily be extended or reused.

The module’s design promotes adaptability. For example, if Grazioso Salvare wanted additional filtering or sorting options, those could be added to the CRUD functions without major adjustments to the dashboard code itself.

## How do you approach a problem as a computer scientist?

As a computer scientist, I approach each problem systematically, focusing first on understanding client needs and then translating those requirements into technical steps. For this project, I began by analyzing the database and dashboard functionality Grazioso Salvare required, then broke down the dashboard’s tasks—data display, filtering, and chart integration—into smaller objectives. Comparing this with past projects, I found the use of MongoDB aggregation pipelines particularly beneficial for complex data requirements, such as grouping by rescue type and counting offices by state.

This structured approach allowed me to address each part of the project incrementally. Moving forward, I would apply these techniques to other database projects, such as incorporating agile principles (e.g., prototyping and feedback cycles) to ensure that client needs are met at every stage of development.

## What do computer scientists do, and why does it matter?

Computer scientists solve real-world problems by creating digital solutions that improve efficiency, accessibility, and decision-making. In this project, my work assists Grazioso Salvare by providing an intuitive interface for quickly identifying dogs suitable for specific rescue tasks. This not only saves the organization time and resources but also ensures that the most capable animals are selected for training. Such projects highlight how technology can be leveraged to support specialized missions like search-and-rescue, ultimately helping organizations like Grazioso Salvare to make a meaningful impact.

---

### Project Features

- **CRUD Python Module**: Connects the MongoDB database with the dashboard widgets, allowing for easy data retrieval, filtering, and manipulation.
- **Interactive Dashboard**: Implements filtering options (by rescue type) with charts and a data table that dynamically update based on user input.
- **Aggregation Pipelines**: Utilizes MongoDB's aggregation pipeline for advanced queries, including total offices by state.

