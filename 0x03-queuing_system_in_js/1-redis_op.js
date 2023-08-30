// Import necessary modules
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Set up event handlers for the Redis client
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Function to set a new school value
function setNewSchool (schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to display the school value
function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error getting value for ${schoolName}: ${err}`);
    } else {
      console.log(`${reply}`);
    }
  });
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
