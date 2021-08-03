DELETE person1 FROM Person person1,
    Person person2
WHERE
    person1.Email = person2.Email AND person1.Id > person2.Id